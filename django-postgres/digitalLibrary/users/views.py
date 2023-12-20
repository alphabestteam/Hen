from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from .models import User

@api_view(['GET','POST'])
def users(request):
    if request.method == 'GET': 
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user_created': True, 'data': serializer.data}, status=200)
        return Response(serializer.errors, status=400)
    
@api_view(['GET','DELETE'])
def get_user(request,email,password):
    if request.method == 'GET':
        users = get_object_or_404(User,email=email,password=password)
        serializer = UserSerializer(users)
        return Response({'user_exist':True,'user':serializer.data},status=200)
    elif request.method == 'DELETE':
        user = get_object_or_404(User,email=email)
        user.delete()
        return Response({'user_deleted': True,"message": "user deleted successfully"})

