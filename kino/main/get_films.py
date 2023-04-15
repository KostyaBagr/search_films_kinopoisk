import requests
import asyncio
import aiohttp
from django.shortcuts import render
headers = {"X-API-KEY": ""}



import aiohttp

# async def get_movies_by_name(request):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(
#             'https://kinobd.ru/api/films') as response:
#             movies = await response.json()
#             print(movies[0])
#
#
#     return render(request, 'main/test.html',{'movies':movies} )
async def get_movies_by_name(name, page=1, limit=10):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(
            'https://api.kinopoisk.dev/v1.2/movie/search',
            params={
                "query": name,
                "limit": limit,
                "page": page,
            }
        ) as response:
            movies = await response.json()
            return movies["docs"]

