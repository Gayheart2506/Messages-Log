from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("hello/<str:name>", views.hello, name="hello"),
    path("about/", views.about_page, name="about"), 
    path("contact/", views.contact_page, name="contact"),
]