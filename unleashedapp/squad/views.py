from rest_framework import generics
from squad.models import Squad
from squad.serializers import SquadSerializer
from rest_framework import permissions
from rest_framework import viewsets

class SquadViewSet(viewsets.ModelViewSet):
    """
    Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /squads/ and /squads/<id>
    """
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer

    def get_object(self):
        if self.request.method == 'PUT':
            squad = Squad.objects.filter(id=self.kwargs.get('pk')).first()
            if squad:
                return squad
            else:
                return Squad(id=self.kwargs.get('pk'))
        else:
            return super(SquadViewSet, self).get_object()