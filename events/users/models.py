from django.db import models
from django.core.exceptions import ValidationError


def validate_email(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('Email must be from example.com domain.')

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name: models.CharField(max_length=20)
    famely_name: models.CharField(max_length=20)
    user_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(validators=[validate_email])
    
