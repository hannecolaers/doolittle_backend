from django.conf.urls import url, include
from rest_framework import routers
from squads import views

router = routers.DefaultRouter()
router.register(r'squads', views.SquadViewSet)
router.register(r'memberships', views.MembershipViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]