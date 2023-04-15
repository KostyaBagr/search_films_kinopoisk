# from django.http import HttpResponse
# from django.shortcuts import render
from django.shortcuts import render
import asyncio
from .get_films import get_movies_by_name
# # Create your views here.
def main_page(request):
    search = request.GET.get('search', '')
    # movies = await get_movies_by_name(f"{search}", page=1, limit=10)
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    movies = asyncio.run(get_movies_by_name(search))

    dict = {
        'name':movies[0]['name'],

        'movies':movies

    }





    return render(request, 'main/home.html', dict)