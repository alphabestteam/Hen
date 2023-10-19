import json
from django.shortcuts import render
from person.models import Person, Parent
from person.serializers import PersonSerializer , ParentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.db.models import Q




@csrf_exempt
def all_persons(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        persons_serialized = PersonSerializer(persons,many = True)
        return JsonResponse(persons_serialized.data,safe=False,status= 200)

@csrf_exempt  
def add_person(request):
    if request.method == 'POST':
        object_data = JSONParser().parse(request)
        data_deserialized = PersonSerializer(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.save()# fix error from part 4 
            return HttpResponse("the person was saved succesfuly!",status=200)
        else:
            return HttpResponse("the object is not well-formed",status=400)

@csrf_exempt
def update_person(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            person_id = data["id"]
            person = Person.objects.get(id=person_id)
            person_serializer = PersonSerializer(person,data=data)
            if person_serializer.is_valid():
                person_serializer.update(person,data)
                return JsonResponse(person_serializer.data,safe=False)
        except:# fix error from part 4 
            return HttpResponse("the object is not well-update",status=400)
        return JsonResponse(person_serializer.errors, status=400)
    
@csrf_exempt
def update_parent(request):
    if request.method == "PUT":
        data = JSONParser().parse(request)
        try:
            parent = Parent.objects.get(id=data["id"])
        except :
            return HttpResponse(
                "object doesn't exist", status=400
            )
        parent_ser = ParentSerializer(parent, data=data)

        if parent_ser.is_valid():
            parent_ser.update(parent, data)
            return HttpResponse("updated!", status=200)
        else:
            return HttpResponse("not updated", status=400)


@csrf_exempt   
def remove_person(request, person_id):
    if request.method == 'DELETE':
        try:
            person = Person.objects.get(id=person_id)
            person.delete()
            return HttpResponse("Person deleted successfully",status=200)
        except:
            return HttpResponse("there was a problem to delete",status=400)
    
@csrf_exempt
def add_parent(request):
    if request.method == 'POST':
        try:
            object_data = JSONParser().parse(request)
            print("good")
            data_deserialized = ParentSerializer(data=object_data)
            if data_deserialized.is_valid():
                data_deserialized.save()
                return HttpResponse("the parent was saved succesfuly!",status=200)
            else:
                return HttpResponse("the object is not well-formed",status=400)
        except:
            return HttpResponse("the object is not well-formed",status=400)
        
@csrf_exempt
def all_parents(request):
    if request.method == 'GET':
        persons = Parent.objects.all()
        persons_serialized = ParentSerializer(persons,many = True)
        return JsonResponse(persons_serialized.data,safe=False,status= 200)
    
@csrf_exempt
def remove_parent(request,parent_id):
    if request.method == 'DELETE':
        try:
            parent = Parent.objects.get(id=parent_id)
            parent.delete()
            return HttpResponse("Parent deleted successfully",status=200)
        except:
            return HttpResponse("there was a problem to delete",status=400)
        
@csrf_exempt
def add_kid(request,parent_id,kid_id):
    if request.method == 'POST':
        try:
            parent = Parent.objects.get(id=parent_id)
            kid = Person.objects.get(id=kid_id)
            if kid.id not in parent.kids.all().values_list('id', flat=True):
                parent.kids.add(kid)
                parent.save()
                return HttpResponse("Kid added successfully to the parent.", status=200)
            else:
                return HttpResponse("Kid is already in the parent's kids list.", status=400)
        except:
            return HttpResponse("cant add person to parent", status=400)

@csrf_exempt
def get_parent_and_kid(request,parent_id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(id=parent_id)
            parent_serialized = ParentSerializer(parent).data
            kids = parent.kids.all()
            kids_serialized = []
            for kid in kids:
                kid_data = PersonSerializer(kid).data
                kids_serialized.append(kid_data)
            result = {
                "parent ":parent_serialized,
                "kids ":kids_serialized,
            }
            return JsonResponse(result,safe=False,status= 200)
        except :
            return HttpResponse("Parent not found.", status=400)

@csrf_exempt
def rich_kid(request):
    if request.method == 'GET':
        try:
            cutoff_birthdate = (datetime.now() - timedelta(days=18 * 365.25)).strftime('%Y-%m-%d')
            print("hello")
            rich_children = Person.objects.filter(
                Q(parents__salary__gte=50000) & Q(birth_data__gt=cutoff_birthdate)
            )
            rich_children_data = [PersonSerializer(rich_child).data for rich_child in rich_children]
            return JsonResponse(rich_children_data, safe=False, status=200)
        except :
            return JsonResponse("cant find richkid",safe=False,status=500)


@csrf_exempt
def find_parents(request,kid_id):
    if request.method == 'GET':
        try:
            kid = Person.objects.get(id=kid_id)
            parents = Parent.objects.all()
            parents_of_kid = []
            for parent in parents:
                if kid.id in parent.kids.all().values_list('id', flat=True):
                    parent_serialized = ParentSerializer(parent).data
                    parents_of_kid.append(parent_serialized)
            return JsonResponse(parents_of_kid,safe=False,status=200)
        except :
            return HttpResponse("Parent not found.", status=400)



@csrf_exempt
def find_kids(request,parent_id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(id=parent_id)
            kids = parent.kids.all()
            kids_serialized = []
            for kid in kids:
                kid_data = PersonSerializer(kid).data
                kids_serialized.append(kid_data)
            result = {
                "kids ":kids_serialized,
            }
            return JsonResponse(result,safe=False,status= 200)
        except :
            return HttpResponse("Parent not found.", status=400)

@csrf_exempt
def find_grand(request,grand_kid_id):
    if request.method == 'GET':
        try:
            grand_kid = Person.objects.get(id=grand_kid_id)
            parents = Parent.objects.all()
            grand_parents_of_kid = []
            for parent in parents:
                if grand_kid.id in parent.kids.all().values_list('id', flat=True):
                    for grand_parent in parents:
                        if parent.id in grand_parent.kids.all().values_list('id',flat=True):
                            grand_parents_serialized = ParentSerializer(parent).data
                            grand_parents_of_kid.append(grand_parents_serialized)
            return JsonResponse(grand_parents_of_kid,safe=False,status=200)
        except :
            return HttpResponse("Parent not found.", status=400)

@csrf_exempt
def find_brothers(request,brother_id):
    if request.method == 'GET':
        try:
            brother = Person.objects.get(id= brother_id)
            parents = Parent.objects.all()
            brothers = []
            for parent in parents:
                if brother.id in parent.kids.all().values_list('id', flat=True):
                    other_brothers = parent.kids.all()
                    for other_brother in other_brothers:
                        if other_brother != brother:
                            if other_brother not in brothers:
                                brother_data = PersonSerializer(other_brother).data
                                brothers.append(brother_data)
            return JsonResponse(brothers,safe=False,status=200)
        except:
            return HttpResponse("cant find brothers", status=400)
                    
