from django.urls import path, include
from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('create_user/', views.create_user, name='create_user'),
    path('create_userk/', views.create_userk, name='create_userk'),
    path('update_name_user/<str:user_name>/',views.update_user_name,name='update_user_name'),
    path('get_all_users/', views.get_all_users, name='get_all_users'),
    path('delete_user/<str:user_name>/', views.delete_user, name='delete_user'),
    path('users_over_age/<int:age>/', views.users_over_age, name='users_over_age'),
    path('users_with_keyword/<str:keyword>/', views.users_with_keyword, name='users_with_keyword'),
    path('add_one_year_to_birthdates/', views.add_one_year_to_birthdates, name='add_one_year_to_birthdates'),
]