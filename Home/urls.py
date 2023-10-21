from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("hello/<str:name>", views.hello, name="hello"),
]