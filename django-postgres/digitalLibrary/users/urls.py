from django.urls import path, include
from . import views

urlpatterns = [
    path('users/',views.users,name='users'),
    path('users/<str:email>/<str:password>/',views.get_user,name='get_user')
]
