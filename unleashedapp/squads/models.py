from django.db import models
from employees.models import Employee

"""
Model class for Squad
"""


class Squad(models.Model):
    name = models.CharField(max_length=40)

"""
Model class for Membership
"""


class Membership(models.Model):
    """
    Define meta data form Membership
    """
    class Meta:
        unique_together = (('employee', 'squad'))

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False, default=1)
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE, null=False, blank=False, default=1)
