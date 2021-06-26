from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView


urlpatterns = [
  path('<str:username>/', ProfileDetailView, name='profile-detail-view'),
  path('update/<int:pk>/user/', ProfileUpdateView.as_view(), name='profile-update-view'),
]