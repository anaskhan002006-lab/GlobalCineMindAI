from recommender.content_based import recommend
from recommender.bollywood_recommender import recommend_bollywood

def global_recommend(movie_name, industry):
    if industry == "Hollywood":
        return recommend(movie_name)
    else:
        return recommend_bollywood(movie_name)