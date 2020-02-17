from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_User = models.BooleanField(default=False)
    is_Company = models.BooleanField(default=False)
    user_level = models.CharField(max_length=20)
    name = models.CharField(max_length=20)