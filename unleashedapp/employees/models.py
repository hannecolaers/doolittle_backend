from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    function = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    visible_site = models.BooleanField()
    # habitat = models.ForeignKey(Habitat, on_delete=models.SET_NULL, null=True, blank=True)
    habitat = models.CharField(max_length=40, null=True, blank=True)

