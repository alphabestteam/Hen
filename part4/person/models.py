from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    birth_data = models.DateField()
    city = models.CharField(max_length=20)
