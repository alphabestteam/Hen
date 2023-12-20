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
def deleteBook(request,user_id,book_id):
    user = get_object_or_404(User, id=user_id)
    try:
        book = get_object_or_404(sellBook, user=user, id=book_id)
    except:
        book = get_object_or_404(borrowBook, user=user, id=book_id)

    book.delete()
    return Response({'book_deleted': True,"message": "Book deleted successfully"})

@api_view(['GET','PUT'])
def getBook(request,book_id):
    if request.method == 'GET':
        try:
            book = get_object_or_404(sellBook,id = book_id)
            serializer = sellBookSerializers(book)
        except:
            book = get_object_or_404(borrowBook,id = book_id)
            serializer = borrowBookSerializers(book)

        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            book = get_object_or_404(sellBook,id = book_id)
            serializer = sellBookSerializers(book, data=request.data)
        except:
            book = get_object_or_404(borrowBook,id = book_id)
            serializer = borrowBookSerializers(book,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'book_update':True,"message":"book update successfully"})

@api_view(['GET'])
def getUserBooks(request,user_id):
    user = get_object_or_404(User, id=user_id)
    borrowBooks = borrowBook.objects.filter(user=user, book_type='Borrow')
    sellBooks = sellBook.objects.filter(user=user, book_type='Sell')

    borrowBooksData = borrowBookSerializers(borrowBooks, many=True).data
    sellBooksData = sellBookSerializers(sellBooks, many=True).data

    return Response({'borrow_books':borrowBooksData,'sell_books':sellBooksData},status=200)
