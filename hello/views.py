from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, Phinehas ! Ceci est un nouveau déploement !")
