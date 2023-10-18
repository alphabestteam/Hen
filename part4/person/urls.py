from django.urls import path
from . import views

urlpatterns = [
    path('api/getAllPeople/',views.all_persons,name='all_persons'),
    path('api/addPerson/',views.add_person,name='add_person'),
    path('api/updatePerson/',views.update_person,name='update_person'),
    path('api/removePerson/<int:person_id>/',views.remove_person,name='remove_person'),
]