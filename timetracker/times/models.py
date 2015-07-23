from django.db import models

from django.utils import timezone

# Create your models here.
class Entry(models.Model):
    start = models.DateTimeField(default=timezone.now)
    stop = models.DateTimeField(blank=True, null=True)
    client = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
