from django.urls import path, include
from . import views

# create url paths.

urlpatterns = [
    path('', views.home, name='webapp-home'),  # insert name of app to specify.
    path('store/', views.store, name='webapp-store'),
]