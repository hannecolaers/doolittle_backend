from rest_framework import serializers
from employees.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('url', 'id', 'first_name', 'last_name', 'function', 'start_date', 'end_date', 'visible_site', 'habitat')
