from django.shortcuts import render
from django.http import HttpResponse

def len_of_word(request,word):
    if word.isalpha():
        return HttpResponse(len(word))
    else:
        return HttpResponse("you got error")

