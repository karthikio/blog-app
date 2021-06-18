from django import forms
from django.contrib.auth.forms import  ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
from .models import User


class UserAdminCreationForm(forms.ModelForm):
  password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('username', 'email',)

  def clean_password(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError('Passwords didn\'t match!')
    return password2

  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password2'])
    if commit:
      user.save()
    return user


class UserAdminChangeForm(forms.ModelForm):
  password = ReadOnlyPasswordHashField()

  class Meta:
    model = User
    fields = ('username', 'email', 'password', 'is_active', 'staff', 'admin')

  def clean_password(self):
    return self.initial['password']



# register form
class RegisterForm(forms.ModelForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Username'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Email Id'}))
  password1 = forms.CharField(widget=forms.PasswordInput(
    attrs = {
      'class': 'form-input',
      'placeholder': 'Password'
    }
  )) 

  password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
    attrs = {
      'class': 'form-input',
      'placeholder': 'Confirm Password'
    }
  ))

  class Meta:
    model = User
    fields = ('email', 'username',)

  def clean_email(self):
    email = self.cleaned_data.get('email')
    qs = User.objects.filter(email=email)
    if qs.exists():
      raise forms.ValidationError('This email is taken.')
    return email

  def clean_username(self):
    username = self.cleaned_data.get('username')
    qs = User.objects.filter(username=username)
    if qs.exists():
      raise forms.ValidationError('This username is taken.')
    return username
    
  def clean_password2(self):
    # checking password1 == password2
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError("Passwords didn't match")
    return password2

  def save(self, commit=True):
    # Save the provided password in hashed format
    user = super(RegisterForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password2"])
    if commit:
      user.save()
    return user




# login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=80,
        widget=forms.TextInput(
            attrs= {
                'class': 'form-input',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-input',
                # 'id': 'user-password',
                'placeholder': 'Password'
            }
        )
    )

    def clean(self):
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')
      if not authenticate(username=username, password=password):
        # raise forms.ValidationError('Invalid username and password.')
        qs = User.objects.filter(username=username)
        if not qs.exists():
          raise forms.ValidationError('This is an invalid username, please pick another.')   
        else:
          raise forms.ValidationError('Incorrect password.')