import requests
import asyncio
import aiohttp
from django.shortcuts import render
headers = {"X-API-KEY": "QTZZHZY-EWZMFB0-K0X7FKZ-V41YB9P"}



import aiohttp

async def get_movies_by_name(name, page=1, limit=40):
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
            if limit == 40:
                page += 1  # увеличиваем номер страницы на 1, если limit=40
            return movies["docs"], page

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# a = asyncio.run(get_movies_by_name('аватар'))
# print(a)

# def get_movies_by_name(name, page = 1, limit = 40):
#     response = requests.get(
#         'https://api.kinopoisk.dev/v1.2/movie/search',
#         params={
#             "query": name,
#             "limit": limit,
#             "page": page,
#         },
#         headers=headers
#     )
#     movies = response.json()
#
#     return movies["docs"]
#
# movies = get_movies_by_name('Человек паук')

