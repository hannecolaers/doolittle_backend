from django.conf.urls import url, include
from rest_framework import routers
from squad import views

router = routers.DefaultRouter()
router.register(r'squads', views.SquadViewSet)
router.register(r'squadsemployees', views.SquadEmployeeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]