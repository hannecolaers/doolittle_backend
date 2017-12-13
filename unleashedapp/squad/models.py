from django.db import models

# Create your models here.
class Squad(models.Model):
    name = models.TextField(max_length=40)