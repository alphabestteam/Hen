from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    birth_data = models.DateField()
    city = models.CharField(max_length=20)

class Parent(Person):
    work_place = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    kids = models.ManyToManyField(Person,related_name="parents", default=[])
