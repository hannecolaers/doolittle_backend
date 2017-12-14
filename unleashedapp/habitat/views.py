from rest_framework import generics
from habitat.models import Habitat
from habitat.serializers import HabitatSerializer
from rest_framework import permissions
from rest_framework import viewsets

class HabitatViewSet(viewsets.ModelViewSet):
    """
    Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /habitats/ and /habitats/<id>
    """
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer