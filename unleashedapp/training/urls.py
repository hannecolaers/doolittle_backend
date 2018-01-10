from django.conf.urls import url
from training import views

urlpatterns = [
    url(r'^training/$', views.training_list),
]