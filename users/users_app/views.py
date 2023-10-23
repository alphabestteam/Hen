from django.shortcuts import render
from .models import User,UserK
from datetime import date, timedelta
from django.views.decorators.csrf import csrf_exempt
from users_app.seralizers import UserSerializer , UserKSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404



@api_view(['POST'])
def create_userk(request):
    serializer = UserKSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):

        userk_name = request.data.get('user', None)
        userk, created = UserK.objects.get_or_create(name=userk_name)

        serializer.validated_data['user'] = userk
        serializer.save()
        return Response(serializer.data)
    
@api_view(['PUT'])
def update_user_name(request, user_name):
    user = get_object_or_404(User,name=user_name)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


   
@api_view(['GET'])
def get_all_users(request):
    age = request.query_params.get('age')
    keyword = request.query_params.get('keyword')
    users = User.objects.all()
    if age:
        users = users.filter(birth_date__lte=date.today() - timedelta(days=int(age) * 365.25))
    if keyword:
        users = users.filter(name__icontains=keyword)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_user(request, user_name):
        user = get_object_or_404(User,name=user_name)
        user.delete()
        return Response({"message": "User deleted successfully"})
    

@api_view(['GET'])
def users_over_age(request, age):
    users = User.objects.filter(birth_date__lte=date.today() - timedelta(days=age * 365.25))
    user_data = [{"name": user.name, "email": user.email, "age": user.age} for user in users]
    return Response(user_data)

@api_view(['GET'])
def users_with_keyword(request, keyword):
    users = User.objects.filter(name__icontains=keyword)
    user_data = [{"name": user.name, "email": user.email, "age": user.age} for user in users]
    return Response(user_data)

@csrf_exempt
@api_view(['POST'])
def add_one_year_to_birthdates(request):
    users = User.objects.all()
    for user in users:
        user.birth_date = user.birth_date + timedelta(days=365)
        user.save()
    user_data = [{"name": user.name, "email": user.email, "age": user.age} for user in users]
    return Response(user_data)

