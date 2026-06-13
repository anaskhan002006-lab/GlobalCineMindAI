import pandas as pd

movies = pd.read_csv("data/bollywood_movies.csv")

movies["Genre"] = movies["Genre"].fillna("")

def recommend_bollywood(movie_name):
    movie = movies[
        movies["Movie Name"].str.lower() == movie_name.lower()
    ]

    if len(movie) == 0:
        return []

    genre = movie.iloc[0]["Genre"]

    recommendations = movies[
        movies["Genre"] == genre
    ]["Movie Name"].head(10)

    return recommendations.tolist()