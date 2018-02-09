from floorplan.models import Room, Space
from floorplan.serializers import RoomSerializer, SpaceSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    """
    Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /rooms/ and /rooms/<id>
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SpaceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    """
    Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /spaces/ and /spaces/<id>
    """
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
