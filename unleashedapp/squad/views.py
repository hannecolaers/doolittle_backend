from rest_framework import generics
from squad.models import Squad
from squad.serializers import SquadSerializer
from rest_framework import permissions
from rest_framework import viewsets

class SquadList(viewsets.ModelViewSet):
    """
    List all squads or create a new squad
    """
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer

class SquadDetail(viewsets.ModelViewSet):
    """
    Retrieve, update or delete a squad.
    """
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer