# from django.http import HttpResponse
# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import asyncio
from django.http import HttpResponseForbidden
from .get_films import get_movies_by_name
# # Create your views here.
async def main_page(request):
    search = request.GET.get('search', '')
    limit = 30
    movies = await get_movies_by_name(search, page=1, limit=limit)

    movie_list = []
    for movie in movies:
        movie_dict = {
            'title':'Поисковик фильмов',
            'name': movie['name'],
            'photo': movie['poster'],
            'link': 'https://www.kinopoisk.ru/film/' + str(movie['id']),
            'rating': movie['rating'],
            'year': movie['year'],
            'description':movie['description'],
            'poster':movie['poster']
        }
        movie_list.append(movie_dict)

    dict = {'movies': movie_list}
    return render(request, 'main/home.html', dict)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')