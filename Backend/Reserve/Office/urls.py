from django.urls import path, include
from . import views

urlpatterns = [
    path("first/", views.first_floor, name="first_floor"),
    path("second/", views.second_floor, name="second_floor"),
    path("third/", views.third_floor, name="third_floor"),
    path("test/", views.first_floor, name="test"),
]