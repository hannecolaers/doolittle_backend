from rest_framework import serializers
import training.models import Training

class TrainingSerializer(serializers.Serializer):
    date = models.DateField()
    days = models.IntegerField()
    firstname = models.TextField(max_length=50)
    lastname = models.TextField(max_length=50)
    team = models.TextField(max_length=50)
    training = models.TextField(max_length=255)
    company = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    invoice = models.TextField(max_length=255)
    info = models.TextField(max_length=255)

    class Meta:
        ordering = ('date',)