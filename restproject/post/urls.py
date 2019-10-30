from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

urlpatterns = [
    path('post/', views.PostList.as_view()), #127.0.0.1:8000/post
    path('post/<int:pk>/', views.PostDetail.as_view()), #127.0.0.1:8000/post/<pk>
]

urlpatterns = format_suffix_patterns(urlpatterns)