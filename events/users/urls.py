from django.urls import path, include
from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('getUser/<int:user_id>/',views.get_user,name='get_user'),
    path('createUser/', views.create_user, name='create_user'),
    path('updateUser/<int:user_id>/',views.update_user,name='update_user'),
    path('getAllUsers/', views.get_all_users, name='get_all_users'),
    path('deleteUser/<int:user_id>/', views.delete_user, name='delete_user'),
]