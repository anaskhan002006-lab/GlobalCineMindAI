import requests

API_KEY = "af5932e198059ed7d31c05854283b84c"

def get_movie_poster(movie_name):

    try:

        search_url = "https://api.themoviedb.org/3/search/movie"

        params = {
            "api_key": API_KEY,
            "query": movie_name
        }

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            search_url,
            params=params,
            headers=headers,
            timeout=10
        )

        data = response.json()

        if data.get("results"):

            poster_path = data["results"][0].get(
                "poster_path"
            )

            if poster_path:

                image_url = (
                    "https://image.tmdb.org/t/p/w500"
                    + poster_path
                )

                image_data = requests.get(
                    image_url,
                    headers=headers,
                    timeout=10
                ).content

                return image_data

    except Exception as e:

        print("TMDB ERROR:", e)

    return None