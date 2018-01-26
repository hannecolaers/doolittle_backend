from rest_framework.response import Response

from employees.models import Employee

# Create your views here.
from rest_framework import viewsets, status
from employees.serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated


class EmployeeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    """
        Provide an endpoint for POST, PUT, PATCH, DELETE and GET on /employees/ and /employees/<id>/
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
