from django.db import models

# Create your models here.

class Book (models.Model):
    Name = models.CharField (max_length=150,
                             primary_key=True,
                             unique=True)