from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class Challenge(models.Model):
    challenge_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rec_user_level = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_by')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participants',
                                     blank=True, null=True)
