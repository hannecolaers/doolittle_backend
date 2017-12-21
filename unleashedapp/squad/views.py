from rest_framework import generics
from squad.models import Squad, SquadEmployee
from squad.serializers import SquadSerializer, SquadEmployeeSerializer, EmployeesInSquadSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

class SquadViewSet(viewsets.ModelViewSet):
    """
    Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /squads/ and /squads/<id>/
    """
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer
    
    """
    Provide a list of all employees within the selected habitat
    """
    @detail_route(methods=['get'])
    def employees(self, request, pk=None):
        squad_id = self.kwargs.get('pk')
        queryset = SquadEmployee.objects.filter(squad_id=squad_id)
        serializer = EmployeesInSquadSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

class SquadEmployeeViewSet(viewsets.ModelViewSet):
    """
    Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /squadsemployees/ and /squadsemployees/<id>/
    """
    queryset = SquadEmployee.objects.all()
    serializer_class = SquadEmployeeSerializer