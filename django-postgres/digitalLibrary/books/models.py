from django.db import models
from users.models import User

class BookType(models.TextChoices):
    BORROW = 'Borrow', 'Borrow'
    SELL = 'Sell', 'Sell'

class borrowBook(models.Model):
    owner_email = models.EmailField(max_length=150,default='')
    book_name = models.CharField(max_length=20)
    author_name = models.CharField(max_length=25)
    user = models.ForeignKey(User,related_name='books',on_delete=models.CASCADE,null=True)
    book_type = models.CharField(max_length=10, choices=BookType.choices, default=BookType.BORROW)

class sellBook(borrowBook):
    price = models.IntegerField()
