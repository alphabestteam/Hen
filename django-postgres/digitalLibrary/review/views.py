from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import reviewSerializers
from books.models import borrowBook, sellBook
from users.models import User
from .models import Review


@api_view(['GET','POST'])
def review(request):
    if request.method == 'GET': 
        reviews = Review.objects.all()
        serializer = reviewSerializers(reviews,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = reviewSerializers(data=request.data)
    
        if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        
@api_view(['GET'])
def bookReview(request, book_id):
    try:
        book = get_object_or_404(sellBook, id=book_id)
        reviews = Review.objects.filter(content_type=3, object_id=book_id)
    except:
        book = get_object_or_404(borrowBook, id=book_id)
        reviews = Review.objects.filter(content_type=2, object_id=book_id)

    serializer = reviewSerializers(reviews, many=True)
    return Response(serializer.data)