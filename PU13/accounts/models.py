from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    CustomUser tar inn AbstractUser som fra tidligere har et 'username'-felt.
    De andre attributtene/feltene er egendefinerte og det er slik de vil bli representert i databasen.
    """
    is_User = models.BooleanField(default=False)
    is_Company = models.BooleanField(default=False)
    user_level = models.CharField(max_length=20)
    name = models.CharField(max_length=20)