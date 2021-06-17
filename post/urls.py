from django.urls import path
from .views import PostDetailView, PostListView, PostFormView


urlpatterns = [
  path('', PostListView.as_view(), name='posts-list-view'),
  path('<int:pk>/', PostDetailView.as_view(), name='posts-detail-view'),
  path('create/', PostFormView.as_view(), name='posts-create-view'),
]