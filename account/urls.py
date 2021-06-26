from django.urls import path
from .views import loginView, logoutView, registerView, contactView, UserDeleteView
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('register/', registerView, name='register-view'),
  path('login/', loginView, name='login-view'),
  path('logout/', logoutView, name='logout-view'),
  path('contact/', contactView, name='contact-view'),
  path('deactivate/<int:pk>/', UserDeleteView.as_view(), name='user-delete-view'),

  # password reset url patterns
  path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html', html_email_template_name='account/password_reset_email.html'), name='password_reset'),

  path('password-reset-request-sent/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
  
  path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),

  path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
]