from django.urls import path
from .views import (
  PostDetailView, PostListView, PostUpdateView, PostCreateView, PostDeleteView
)

urlpatterns = [
  path('', PostListView.as_view(), name='posts-list-view'),
  path('detail/<int:pk>/', PostDetailView.as_view(), name='posts-detail-view'),
  path('create/', PostCreateView.as_view(), name='posts-create-view'),
  path('post/update/<int:pk>/', PostUpdateView.as_view(), name='posts-update-view'),
  path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='posts-delete-view'),
]