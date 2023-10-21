from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

# Create your views here.

def home(request):
    return HttpResponse("Hello Django, this is my website")

def hello(request, name):
    return render(request, "hello/index.html", {
        "name": name, 
        "date": datetime.now()
    })
