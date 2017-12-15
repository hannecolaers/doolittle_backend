from django.utils.encoding import force_text
from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from employees.models import Employee
from habitat.models import Habitat
from habitat.serializers import HabitatSerializer


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    habitat = HabitatSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'function',
                  'start_date', 'end_date', 'visible_site', 'habitat')

    def create(self, validated_data):
        habitat_data = validated_data.pop('habitat')
        employee = Employee.objects.create(**validated_data)
        if Habitat.objects.filter(name=habitat_data["name"]).exists():
            Habitat.objects.get(**habitat_data)
            habitat = Habitat.objects.get(name=habitat_data["name"])
            employee.habitat = habitat
            return employee
        else:
            raise InvalidHabitatError()

    def update(self, employee, validated_data):
        employee.first_name = validated_data.get('first_name', employee.first_name)
        employee.last_name = validated_data.get('last_name', employee.last_name)
        employee.function = validated_data.get('function', employee.function)
        employee.start_date = validated_data.get('start_date', employee.start_date)
        employee.end_date = validated_data.get('end_date', employee.end_date)
        employee.visible_site = validated_data.get('visible_site', employee.visible_site)
        if validated_data.get('habitat'):
            habitat_name = validated_data.get('habitat').get('name')
            habitat = Habitat.objects.get(name=habitat_name)
            employee.habitat = habitat
        return employee


class InvalidHabitatError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Habitat does not exist"

