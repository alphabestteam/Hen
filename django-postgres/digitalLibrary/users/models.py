from django.db import models
from django.core.exceptions import ValidationError


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=25,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    id_admin = models.BooleanField(default=False)