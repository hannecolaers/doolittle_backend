from employees.models import Employee
from employees.serializers import EmployeeSerializer
from habitats.models import Habitat
from habitats.serializers import HabitatSerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HabitatViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    """
    Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /habitats/ and /habitats/<id>/
    """
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer

    """
    Provide a list of all employees within the selected habitat
    """

    @detail_route(methods=['get'])
    def employees(self, request, pk=None):
        habitat_id = self.kwargs.get('pk')
        queryset = Employee.objects.filter(habitat=habitat_id)
        serializer = EmployeeSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)
