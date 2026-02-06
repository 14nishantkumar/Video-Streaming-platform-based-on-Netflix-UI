import random as rnd
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse
from django.http import JsonResponse

from .forms import ProfileForm
from .models import Profile

from .services.tmdb import (
    fetch_trending_movies,
    fetch_popular_movies,
    fetch_top_rated_movies,
    fetch_movie_detail,
    fetch_movie_trailer,
    fetch_kids_movies
)


# LANDING
def landing(request):
    """
    Public landing page.
    Logged-in users go to profile selection.
    """
    if request.user.is_authenticated:
        return redirect("netflixapp:profile-list")

    return render(request, "landing.html")


# PROFILE LIST 
@login_required
def ProfileList(request):
    profiles = Profile.objects.filter(user=request.user)
    return render(request, "profilelist.html", {"profiles": profiles})


# PROFILE CREATE
class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profilecreate.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("netflixapp:profile-list")


# PROFILE DELETE 
@login_required
def ProfileDelete(request, uuid):
    profile = get_object_or_404(Profile, uuid=uuid, user=request.user)

    if request.method == "POST":
        profile.delete()
        return redirect("netflixapp:profile-list")

    return render(request, "profile_delete_confirm.html", {"profile": profile})


#HOME 
@login_required
def home(request, profile_uuid):
    
    profile = get_object_or_404(Profile, uuid=profile_uuid, user=request.user)

    
    if profile.is_kid:
        movies = fetch_kids_movies(page=1)
        trending = fetch_kids_movies(page=1)
    else:
        movies = fetch_popular_movies(page=1)
        trending = fetch_trending_movies(page=1)

    banner_movie = rnd.choice(trending) if trending else None

    return render(
        request,
        "home.html",
        {
            "profile": profile,
            "movies": movies,
            "banner_movie": banner_movie,
        },
    )


# MOVIE DETAIL 
@login_required
def movie_detail(request, profile_uuid, movie_id):
    """
    Movie info page with trailer.
    """
    profile = get_object_or_404(Profile, uuid=profile_uuid, user=request.user)

    movie = fetch_movie_detail(movie_id)
    trailer_key = fetch_movie_trailer(movie_id)

    return render(
        request,
        "movie_detail.html",
        {
            "movie": movie,
            "trailer_key": trailer_key,
            "profile": profile,
        },
    )

@login_required
def load_more_movies(request):
    page = int(request.GET.get("page", 1))
    category = request.GET.get("category", "popular")

    category_map = {
        "popular": fetch_popular_movies,
        "trending": fetch_trending_movies,
        "top_rated": fetch_top_rated_movies,
    }

    fetch_function = category_map.get(category, fetch_popular_movies)
    movies = fetch_function(page)

    return JsonResponse({"movies": movies})


@method_decorator(login_required, name='dispatch')
class MovieList(View):
    def get(self, request, profile_uuid, *args, **kwargs):
        profile = get_object_or_404(
            Profile,
            uuid=profile_uuid,
            user=request.user
        )

        page = int(request.GET.get("page", 1))

        if profile.is_kid:
            movies = fetch_kids_movies(page=page)
        else:
            movies = fetch_popular_movies(page=page)

        context = {
            "profile": profile,
            "movies": movies,
            "page": page,
            "next_page": page + 1,
            "prev_page": page - 1 if page > 1 else None,
        }

        return render(request, "movielist.html", context)