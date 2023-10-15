from django.shortcuts import render
from django.http import HttpResponse
import time

def get_time(request):
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    return HttpResponse(curr_time)

