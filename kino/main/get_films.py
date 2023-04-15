import requests
import ast
headers = {"X-API-KEY": "QTZZHZY-EWZMFB0-K0X7FKZ-V41YB9P"}

def get_movies_by_name(name, page = 1, limit = 40):
    response = requests.get(
        'https://api.kinopoisk.dev/v1.2/movie/search',
        params={
            "query": name,
            "limit": limit,
            "page": page,
        },
        headers=headers
    )
    movies = response.json()
    while movies['page'] < movies['pages']:
        for i in range(page, page + limit, 40):
            print(i)
            page += limit
            return movies["docs"]

movies = get_movies_by_name('Человек паук')

