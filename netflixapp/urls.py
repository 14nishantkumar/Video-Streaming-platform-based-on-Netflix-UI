from django.urls import path
from . import views

app_name = 'netflixapp'

urlpatterns = [
    path("", views.landing, name="landing"),

    # profile
    path("profiles/", views.ProfileList, name="profile-list"),
    path("profiles/create/", views.ProfileCreate.as_view(), name="create-profile"),
    path("profile/<uuid:uuid>/delete/", views.ProfileDelete, name="profile-delete"),

    # home
    path("browse/<uuid:profile_uuid>/", views.home, name="home"),

    # movie
    path("watch/<uuid:profile_uuid>/<int:movie_id>/", views.movie_detail, name="movie-detail"),
    path("movies/<uuid:profile_uuid>/",views.MovieList.as_view(),name="movie-list"
),
]
