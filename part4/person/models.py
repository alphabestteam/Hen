from django.db import models
from datetime import datetime


class Person(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    birth_data = models.DateField()
    city = models.CharField(max_length=20)

    def is_adult(self):
        cutoff_age = datetime.now().year - 18
        return self.birth_data.year <= cutoff_age

class Parent(Person):
    work_place = models.CharField(max_length=30)
    salary = models.IntegerField()
    kids = models.ManyToManyField(Person,related_name="parents", default=[])
