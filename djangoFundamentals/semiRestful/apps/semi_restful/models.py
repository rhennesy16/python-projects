from django.db import models

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)