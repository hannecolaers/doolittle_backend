from django.conf.urls import url, include
from rest_framework import routers
from habitats import views

router = routers.DefaultRouter()
router.register(r'habitats', views.HabitatViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]