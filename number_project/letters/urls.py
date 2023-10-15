from django.urls import path
from . import views

urlpatterns = [
    path('api/getLenOfWord/<word>', views.len_of_word, name="get_len_of_word"),
]