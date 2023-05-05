from django.urls import path
from . import views
from .views import Client

urlpatterns = [
    path("", views.home, name="home"),
    path("service", views.service, name="service"),
    path("appointment", Client.as_view(), name="add"),
]
