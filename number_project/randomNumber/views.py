from django.shortcuts import render
from django.http import HttpResponse
import random

def randomNubmer(request):
    final_number = random.uniform(0, 1)
    return HttpResponse(final_number)

def clinteRandomNubmer(request,number):
    try:
        number= int(number)
    except ValueError:
        return HttpResponse("you need to put number")
    if number < 0:
        return HttpResponse("the number need to be bigger than 0")
    
    final_number = random.uniform(0,number)
    return HttpResponse(final_number)


# Create your views here.
