from floorplan.models import Room, Space
from floorplan.serializers import RoomSerializer, SpaceSerializer
from rest_framework import viewsets


class RoomViewSet(viewsets.ModelViewSet):
    """
    Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /rooms/ and /rooms/<id>
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SpaceViewSet(viewsets.ModelViewSet):
    """
    Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /spaces/ and /spaces/<x,y>
    """
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
