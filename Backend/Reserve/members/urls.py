from django.urls import path

# my views
from . import views


urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name='logout'),
    path('profile/', views.profileView, name="profile"),
    path('edit/<int:profile_id>/', views.profileEdit, name="edit"),
    path('edit/change_password/', views.PasswordChangeView.as_view(template_name='Members/password.html'), name='password_change'),
]