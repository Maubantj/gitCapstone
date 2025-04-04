"""
URL configuration for capstone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# Not done in app url.py
from django.contrib.auth import views as auth_views 
from django.urls import path, include
# Not done in app url.py, we modified the registration view in our app.
from user_auth import views as regstr_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # Below four paths not repeated in app url.py. I used django standard views.
    path('register/', regstr_views.register, name='register'),
    path('profile/', regstr_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(
       template_name='user_auth/login.html'), name='login'
       ),
    path('logout/', auth_views.LogoutView.as_view(
       template_name='user_auth/logout.html'), name='logout'
       ),
    path('', include('webapp.urls')),
    path('blog/', include('blog.urls')),
]