from django.urls import path
from  .views import *
from .get_films import *
urlpatterns = [
    path('', main_page, name='main_page')

]