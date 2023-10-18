import json
from django.shortcuts import render
from person.models import Person
from person.serializers import PersonSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

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
            data_deserialized.create(object_data)
            return HttpResponse("the person was saved succesfuly!")
        else:
            return HttpResponse("the object is well-formed")

@csrf_exempt
def update_person(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        person_id = data["id"]
        person = Person.objects.get(id=person_id)
        person_serializer = PersonSerializer(person,data=data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data,safe=False)
        return JsonResponse(person_serializer.errors, status=400)

@csrf_exempt   
def remove_person(request, person_id):
    if request.method == 'DELETE':
        person = Person.objects.get(id=person_id)
        person.delete()
        return HttpResponse("Person deleted successfully",status=200)