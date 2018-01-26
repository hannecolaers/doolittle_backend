from django.forms import ChoiceField
from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from employees.models import Employee
from habitats.models import Habitat
from habitats.serializers import HabitatSerializer


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    habitat = HabitatSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'function',
                  'start_date', 'end_date', 'visible_site', 'picture_url', 'motivation', 'expectations', 'need_to_know', 'date_of_birth', 'gender', 'email', 'habitat')

    def create(self, validated_data):
        habitat_data = validated_data.pop('habitat')
        if Habitat.objects.filter(name=habitat_data["name"]).exists():
            habitat = Habitat.objects.get(name=habitat_data["name"])
            employee = Employee.objects.create(**validated_data)
            employee.habitat = habitat
            return employee
        else:
            raise InvalidHabitatError()

    def update(self, employee, validated_data):
        employee.first_name = validated_data.get('first_name', employee.first_name)
        employee.last_name = validated_data.get('last_name', employee.last_name)
        employee.function = validated_data.get('function', employee.function)
        employee.start_date = validated_data.get('start_date', employee.start_date)
        end_date = validated_data.get('end_date', employee.end_date)
        if end_date < employee.start_date:
            raise InvalidEndDateError()
        employee.end_date = end_date
        employee.visible_site = validated_data.get('visible_site', employee.visible_site)
        if validated_data.get('habitat'):
            habitat_name = validated_data.get('habitat').get('name')
            if Habitat.objects.filter(name=habitat_name).exists():
                habitat = Habitat.objects.get(name=habitat_name)
                employee.habitat = habitat
            else:
                raise InvalidHabitatError()
        employee.picture_url = validated_data.get('picture_url', employee.picture_url)
        employee.motivation = validated_data.get('motivation', employee.motivation)
        employee.expectations = validated_data.get('expectations', employee.expectations)
        employee.need_to_know = validated_data.get('need_to_know', employee.need_to_know)
        employee.date_of_birth = validated_data.get('date_of_birth', employee.date_of_birth)
        employee.gender = validated_data.get('gender', employee.gender)
        employee.email = validated_data.get('email', employee.email)
        employee.save()
        return employee


class InvalidHabitatError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Habitat does not exist"


class InvalidEndDateError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "The end date has to be after the start date"

