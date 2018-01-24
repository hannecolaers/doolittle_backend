from django.conf.urls import url, include
from rest_framework import routers
from floorplan import views

router = routers.DefaultRouter()
router.register(r'spaces', views.SpaceViewSet)
router.register(r'rooms', views.RoomViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
