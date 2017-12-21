from rest_framework import serializers, status
from squad.models import Squad, SquadEmployee
from employees.models import Employee
from employees.serializers import EmployeeSerializer
from rest_framework.exceptions import APIException

class SquadSerializer(serializers.Serializer):
    class Meta:
        model = Squad
        fields = ('name')

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Squad` instance, given the validated data.
        """
        return Squad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Squad` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class SquadEmployeeSerializer(serializers.Serializer):
    class Meta:
        model = SquadEmployee
        fields = ('employee_id', 'squad_id')

    squad = SquadSerializer()
    employee = EmployeeSerializer()

    def create(self, validated_data):
        """
        Create and return a new `SquadEmployee` instance, given the validated data.
        """
        return SquadEmployee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `SquadEmployee` instance, given the validated data.
        """
        instance.squad_id = validated_data.get('squad_id', instance.squad_id)
        instance.employee_id = validated_data.get('employee_id', instance.employee_id)
        instance.save()
        return instance

class EmployeesInSquadSerializer(serializers.Serializer):
    class Meta:
        model = SquadEmployee
        fields = ('employee_id')

    employee = EmployeeSerializer()

    def create(self, validated_data):
        """
        Create and return a new `SquadEmployee` instance, given the validated data.
        """
        return SquadEmployee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `SquadEmployee` instance, given the validated data.
        """
        instance.squad_id = validated_data.get('squad_id', instance.squad_id)
        instance.employee_id = validated_data.get('employee_id', instance.employee_id)
        instance.save()
        return instance