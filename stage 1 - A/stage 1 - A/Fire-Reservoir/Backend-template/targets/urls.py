from django.urls import path
from . import views  

urlpatterns = [
    path('api/targets/AddTarget/', views.add_target, name='add_target'),
    path('api/targets/AllTargets/', views.all_targets, name='all_targets'),
    path('api/targets/UpdateTarget/',views.update_target,name='update_target'),
]
