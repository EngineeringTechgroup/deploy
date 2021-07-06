from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')
