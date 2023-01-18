"""Reserve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# import view from members to make login page as first page

from members import views
from Office import views as officeViews


urlpatterns = [
    path('admin/', admin.site.urls),
    # office app
    path('office/', include('Office.urls')),
    # member app
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    # first page
    path('', views.login_user, name="login"),
    # register page
    path('register/', views.register_profile, name="register"),
    # other single param. urls
    path('settings/', include('Office.urls')),
    path('reserved/', officeViews.reservedViews, name='reserved'),
    path('reserved_delete/<reserve_id>/', officeViews.reserveDelete, name='reserveDelete'),
]
