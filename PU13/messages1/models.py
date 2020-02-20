from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Messages1(models.Model):
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return '{}/{}'.format(self.subject, self.description)
