from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name='logout'),
    path('profile/', views.profileView, name="profile"),
    path('edit/<int:profile_id>/', views.profileEdit, name="edit"),
]