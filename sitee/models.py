from django.db import models

# Create your models here.

class comments(models.Model):
    email=models.EmailField()
    comment=models.TextField()