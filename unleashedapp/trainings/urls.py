from django.conf.urls import url, include
from rest_framework import routers
from trainings import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^trainings/$', views.training_list),
    url(r'^trainings/(?P<lookup>\w+)/$', views.training_employee_list),
]