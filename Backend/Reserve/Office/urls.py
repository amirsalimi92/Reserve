from django.urls import path, include

# my views
from . import views

urlpatterns = [
    path("first/", views.first_floor, name="first_floor"),
    path("second/", views.second_floor, name="second_floor"),
    path("third/", views.third_floor, name="third_floor"),
    path("about/", views.about_page, name="about"),
    path('report/', views.bugReportView, name='report'),
    path('post/', views.post_view, name="post"),
    path('post_delete/<post_id>', views.postDelete, name='delete_post'),
]