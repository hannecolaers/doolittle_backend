"""unleashedapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet
from floorplan.views import RoomViewSet, SpaceViewSet
from squads.views import SquadViewSet, MembershipViewSet
from habitats.views import HabitatViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'spaces', SpaceViewSet)
router.register(r'squads', SquadViewSet)
router.register(r'squads', MembershipViewSet)
router.register(r'habitats', HabitatViewSet)
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('trainings.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
]
