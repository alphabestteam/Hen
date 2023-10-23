from django.db import models
from django.core.exceptions import ValidationError

def validate_email(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('Email must be from example.com domain.')

class UserK(models.Model):
    name = models.CharField(max_length=100, unique=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[validate_email])
    birth_date = models.DateField()
    user = models.ForeignKey(UserK, on_delete=models.CASCADE)

class Message(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
