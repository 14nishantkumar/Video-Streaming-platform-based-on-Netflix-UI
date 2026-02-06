import requests
from django.conf import settings

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"



def _tmdb_request(endpoint, params=None):
    if params is None:
        params = {}

    params["api_key"] = settings.TMDB_API_KEY
    params["language"] = "en-US"

    response = requests.get(f"{BASE_URL}{endpoint}", params=params)

    if response.status_code == 200:
        return response.json()

    return {}

# Fetch movies

def fetch_movies(endpoint, page=1):
    data = _tmdb_request(endpoint, {"page": page})
    return data.get("results", [])



def fetch_trending_movies(page=1):
    return fetch_movies("/trending/movie/week", page)


def fetch_popular_movies(page=1):
    return fetch_movies("/movie/popular", page)


def fetch_top_rated_movies(page=1):
    return fetch_movies("/movie/top_rated", page)


def fetch_kids_movies(page=1):
    data = _tmdb_request(
        "/discover/movie",
        {
            "page": page,
            "certification_country": "US",
            "certification.lte": "PG",
            "with_genres": "16,10751",  
            "sort_by": "popularity.desc"
        }
    )
    return data.get("results", [])



def fetch_movie_detail(tmdb_id):
    return _tmdb_request(f"/movie/{tmdb_id}")



def fetch_movie_trailer(tmdb_id):
    data = _tmdb_request(f"/movie/{tmdb_id}/videos")

    for video in data.get("results", []):
        if video.get("site") == "YouTube" and video.get("type") == "Trailer":
            return video.get("key")

    return None
