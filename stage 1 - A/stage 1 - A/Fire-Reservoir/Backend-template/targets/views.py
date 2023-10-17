import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from targets.models import Target
from targets.serializers import TargetSerializer


@csrf_exempt
def add_target(request):
    if request.method == 'POST':
        object_data = JSONParser().parse(request)
        data_deserialized = TargetSerializer(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.create(object_data)
            return HttpResponse("the target was saved succesfuly!")
        else:
            return HttpResponse("the object is not well-formed")

@csrf_exempt
def update_target(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        target_id = data["target_id"]
        target = Target.objects.get(target_id=target_id)
        target_serializer = TargetSerializer(target,data=data)
        if target_serializer.is_valid():
            target_serializer.save()
            return JsonResponse(target_serializer.data,safe=False)
        return JsonResponse(target_serializer.errors, status=400)

def all_targets(request):
    if request.method == 'GET':
        targets = Target.objects.all()
        targets_serialized = TargetSerializer(targets, many = True)
        return JsonResponse(targets_serialized.data,safe=False,status=200)
