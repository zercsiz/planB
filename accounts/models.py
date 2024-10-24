from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse


class MyAccountManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("username")
        user = self.model(
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    username = models.CharField(max_length=250, unique=True, null=False, blank=False)
    image = models.ImageField(blank=True, null=True, upload_to="images/")
    email = models.EmailField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
