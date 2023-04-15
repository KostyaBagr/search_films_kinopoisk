from django.http import HttpResponse
from django.shortcuts import render
from .get_films import get_movies_by_name
# Create your views here.
def main_page(request):
    search = request.GET.get('search', '')
    movies = get_movies_by_name(search)



    dict = {
        'name': movies[0]['name'],
        'description': movies[0]['description'],
        'countries': movies[0]['countries'],
        'year': movies[0]['year'],
        'movies': movies
    }
    return render(request, 'main/home.html', dict)