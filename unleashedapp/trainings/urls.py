from django.conf.urls import url, include
from trainings import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^trainings/$', views.TrainingList.as_view()),
    url(r'^trainings/(?P<id>\w+)/$', views.TrainingDetail.as_view()),
    url(r'^trainings/(?P<firstname>\w+)/(?P<lastname>\w+)/$', views.TrainingAllDetail.as_view()),
]