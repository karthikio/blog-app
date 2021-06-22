from django.urls import path
from .views import loginView, logoutView, registerView

urlpatterns = [
  path('register/', registerView, name='register-view'),
  path('login/', loginView, name='login-view'),
  path('logout/', logoutView, name='logout-view'),
]