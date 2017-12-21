from django.db import models
from employees.models import Employee

"""
Model class for Squad
"""
class Squad(models.Model):
    name = models.TextField(max_length=40)

"""
Model class for SquadEmployee
"""
class SquadEmployee(models.Model):
    """
    Define meta data form SquadEmployee
    """
    class Meta:
        unique_together = (('employee', 'squad'))

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=True, default=1)
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE, null=False, blank=True, default=1)
