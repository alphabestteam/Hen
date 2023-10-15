from django.urls import path
from randomNumber import views

urlpatterns = [
    path('api/getRandomNumber$', views.randomNubmer, name='get_random_number'),
    path('api/getRandomNumber/(?P<number>\d+)$', views.clinteRandomNubmer, name='get_client_random_number'),
]
