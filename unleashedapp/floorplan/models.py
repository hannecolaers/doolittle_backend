from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=30)


class Space(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    employee_id = models.IntegerField(default=0)
    room_id = models.IntegerField(default=0)