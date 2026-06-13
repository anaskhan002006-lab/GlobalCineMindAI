from tmdb_api import get_movie_poster

movies = [
    "Toy Story",
    "Avatar",
    "Titanic",
    "3 Idiots",
    "Dangal"
]

for movie in movies:
    print("=" * 50)
    print("Movie:", movie)

    poster = get_movie_poster(movie)

    print("Poster:", poster)