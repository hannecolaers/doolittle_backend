from django.conf.urls import url, include
from rest_framework import routers
from squad import views

router = routers.DefaultRouter()
router.register(r'squads', views.SquadList)
#router.register(r'squads/(?P<pk>[0-9]+)/', views.SquadDetail)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]