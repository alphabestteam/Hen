from django.urls import path
from . import views

urlpatterns = [
    path('getAllPeople/',views.all_persons,name='all_persons'),
    path('addPerson/',views.add_person,name='add_person'),
    path('updatePerson/',views.update_person,name='update_person'),
    path('removePerson/<int:person_id>/',views.remove_person,name='remove_person'),


    path('addParent/',views.add_parent,name='add_parent'),#
    path('getAllParents/',views.all_parents,name='all_parents'),#
    path('removeParent/<int:parent_id>/',views.remove_parent,name='remove_parent'),#
    path('updateParent/',views.update_parent,name='update_parent'),#
    path('addKid/<int:parent_id>/<int:kid_id>/',views.add_kid,name='add_kid'),#
    path('getParentAndKid/<int:parent_id>/',views.get_parent_and_kid,name='get_parent_and_kid'),#
    path('richKid/',views.rich_kid,name='rich_kid'),#
    path('findParents/<int:kid_id>/',views.find_parents,name='find_parents'),#
    path('findKids/<int:parent_id>/',views.find_kids,name='find_kids'),#
    path('findGrand/<int:grand_kid_id>/',views.find_grand,name='find_grand'),#
    path('findBrothers/<int:brother_id>/',views.find_brothers,name='find_brothers')#
]