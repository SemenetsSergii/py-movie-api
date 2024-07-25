from django.urls import path
from cinema.models import Movie


app_name = 'cinema'

urlpatterns = [
    path('movies/', movies_list, name='movies_list'),
]