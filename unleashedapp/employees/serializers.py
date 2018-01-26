from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        unique_together = (("first_name", "last_name", "date_of_birth"),)
        depth = 0

    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        return employee

    def update(self, employee, validated_data):
        employee.first_name = validated_data.get('first_name', employee.first_name)
        employee.last_name = validated_data.get('last_name', employee.last_name)
        employee.function = validated_data.get('function', employee.function)
        employee.start_date = validated_data.get('start_date', employee.start_date)
        end_date = validated_data.get('end_date', employee.end_date)
        if end_date and end_date < employee.start_date:
            raise InvalidEndDateError()
        employee.end_date = end_date
        employee.visible_site = validated_data.get('visible_site', employee.visible_site)
        employee.habitat = validated_data.get('habitat', employee.habitat)
        employee.picture_url = validated_data.get('picture_url', employee.picture_url)
        employee.motivation = validated_data.get('motivation', employee.motivation)
        employee.expectations = validated_data.get('expectations', employee.expectations)
        employee.need_to_know = validated_data.get('need_to_know', employee.need_to_know)
        employee.date_of_birth = validated_data.get('date_of_birth', employee.date_of_birth)
        employee.gender = validated_data.get('gender', employee.gender)
        employee.email = validated_data.get('email', employee.email)
        employee.save()
        return employee


class InvalidEndDateError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "The end date has to be after the start date"

