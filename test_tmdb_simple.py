import requests

url = "https://api.themoviedb.org/3/search/movie?api_key=af5932e198059ed7d31c05854283b84c&query=Toy Story"

r = requests.get(url, verify=False, timeout=20)

print(r.status_code)
print(r.text[:200])