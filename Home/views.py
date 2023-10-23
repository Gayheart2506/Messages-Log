from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

# Create your views here.

def home(request):
    return render(request, "hello/home.html")

def hello(request, name):
    return render(request, "hello/index.html", {
        "name": name, 
        "date": datetime.now()
    })

def about_page(request):
    return render(request, "hello/about.html")

def contact_page(request):
    return render(request, "hello/contact.html")
