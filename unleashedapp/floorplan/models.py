from django.db import models
from employees.models import Employee


class Room(models.Model):
    KITCHEN = 'Kitchen'
    EMPTY = 'Empty'
    WORKSPACE = 'Workspace'
    TYPE_CHOICES = (
        (KITCHEN, 'Kitchen'),
        (EMPTY, 'Empty'),
        (WORKSPACE, 'Workspace'),
    )
    name = models.CharField(max_length=30)
    type = models.CharField(choices=TYPE_CHOICES, max_length=30, null=False, blank=False, default=WORKSPACE)
    color = models.CharField(max_length=8, null=False, blank=False, default='FFFFFF')


class Space(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=False, blank=False, default=1)
