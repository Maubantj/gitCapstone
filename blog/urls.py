from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # Use my own name for the home page for easy reference outside of blog app.
    path('', PostListView.as_view(), name='blog-home'),
    # Use django naming convention for detail view as this is within blog app.
    # <app>/<model>_<viewtype>.html 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # Use django naming convention for post create.
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # Django uses the post create form.
    path('post/<int:pk>/update/', PostUpdateView.as_view(),
         name='post-update'
         ),
    # Use django naming convention for post delete.
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),
         name='post-delete'),
]