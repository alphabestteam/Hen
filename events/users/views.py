from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

@api_view(['DELETE'])
def delete_user(request, user_id):
    user = get_object_or_404(User,id=user_id)
    user.delete()
    return Response({"message": "User deleted successfully"})

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request,user_id):
    users = get_object_or_404(User,id=user_id)
    serializer = UserSerializer(users)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['PUT'])
def update_user(request, user_id):
    user = get_object_or_404(User,id=user_id)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

