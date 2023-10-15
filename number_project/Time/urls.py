from django.urls import re_path
from Time import views

urlpatterns = [
    re_path(r'^api/getSErverTime$', views.get_time, name='get_time'),
]