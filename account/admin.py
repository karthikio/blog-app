from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import  UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import  User


admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
  form = UserAdminChangeForm
  add_form = UserAdminCreationForm

  list_display = ('username', 'email', 'is_active', 'staff', 'admin')
  search_fields = ('username', 'email')
  readonly_fields = ('id',)

  filter_horizontal = ()
  list_filter = ()
  fieldsets = ()

admin.site.register(User, UserAdmin)