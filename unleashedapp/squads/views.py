from squads.models import Squad, Membership
from squads.serializers import SquadSerializer, MembershipSerializer, EmployeesInSquadSerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SquadViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

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
        queryset = Membership.objects.filter(squad_id=squad_id)
        serializer = EmployeesInSquadSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)


class MembershipViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    """
    Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /squadsemployees/ and /squadsemployees/<id>/
    """
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
