from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import borrowBookSerializers, sellBookSerializers
from .models import borrowBook, sellBook
from users.models import User


@api_view(['GET','POST'])
def uploadBook(request):
    if request.method == 'GET': 
        books = borrowBook.objects.all()
        serializer = borrowBookSerializers(books,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        book_type = request.data.get('book_type', '').lower()
        if book_type == 'borrow':
            serializer = borrowBookSerializers(data=request.data)
        elif book_type == 'sell':
            serializer = sellBookSerializers(data=request.data)
        else:
            return Response({"error": "Choose 'Borrow' or 'Sell'."}, status=400)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'book_created': True, 'data': serializer.data}, status=200)
        
@api_view(['DELETE'])
def deleteBook(request,user_id,book_name):
    user = get_object_or_404(User, id=user_id)
    try:
        book = get_object_or_404(sellBook, user=user, book_name=book_name)
    except:
        book = get_object_or_404(borrowBook, user=user, book_name=book_name)

    book.delete()
    return Response({"message": "Book deleted successfully"})

@api_view(['GET'])
def getBook(request,book_id):
    try:
        book = get_object_or_404(sellBook,id = book_id)
        serializer = sellBookSerializers(book)
    except:
        book = get_object_or_404(borrowBook,id = book_id)
        serializer = borrowBookSerializers(book)

    return Response(serializer.data)

@api_view(['GET'])
def getUserBooks(request,user_id):
    user = get_object_or_404(User, id=user_id)
    borrowBooks = borrowBook.objects.filter(user=user)
    sellBooks = sellBook.objects.filter(user=user)

    borrowBooksData = borrowBookSerializers(borrowBooks, many=True).data
    sellBooksData = sellBookSerializers(sellBooks, many=True).data

    return Response({'borrow_books':borrowBooksData,'sell_books':sellBooksData},status=200)
