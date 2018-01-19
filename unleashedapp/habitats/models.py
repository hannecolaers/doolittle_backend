from django.db import models

# Create your models here.
class Habitat(models.Model):
    name = models.TextField(max_length=40)