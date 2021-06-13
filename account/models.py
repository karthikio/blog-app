from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('User must have an username')
        if not email:
            raise ValueError('User must have an email id')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuer(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password = password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password = password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(verbose_name='Username', max_length=80, unique=True)
    email = models.EmailField(verbose_name='Email Id', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    # username_field should be unique
    USERNAME_FIELD = 'username'
    # username_field and password is required by default
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return str(self.username)

    # Does the user have specific permission?
    def has_perm(self, perm,obj=None):
        return True

    # Does the user have permission to view app_label
    def has_module_perms(self, app_label):
        return True

    # Is the user is admin
    @property
    def is_admin(self):
        return self.admin

    # Is the user is staff
    @property
    def is_staff(self):
        return self.staff

    # Is the user is staff
    @property
    def active(self):
        return self.is_active

