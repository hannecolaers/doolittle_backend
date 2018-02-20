from django.core.validators import EmailValidator
from django.db import models

# Create your models here.
from django.db.models.functions import Substr, Upper, Lower

from habitats.models import Habitat


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'X'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    function = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    visible_site = models.BooleanField()
    habitat = models.ForeignKey(Habitat, on_delete=models.SET_NULL, null=True, blank=True)
    motivation = models.TextField(null=True, blank=True)
    expectations = models.TextField(null=True, blank=True)
    need_to_know = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    picture_url = models.URLField()
    email = models.EmailField(validators=[EmailValidator(whitelist=['unleashed.be'])])

    def save(self, *args, **kwargs):
        self.first_name = self.first_name[0].upper() + self.first_name[1:].lower()
        return super(Employee, self).save(*args, **kwargs)


    def __str__(self):
        return "%s" % self.first_name + " " + self.last_name

