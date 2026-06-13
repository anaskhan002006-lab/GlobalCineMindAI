import requests

url = "https://api.themoviedb.org/3/search/movie"

params = {
    "api_key": "af5932e198059ed7d31c05854283b84c",
    "query": "Toy Story"
}

response = requests.get(url, params=params, timeout=30)

print(response.status_code)
print(response.text[:500])