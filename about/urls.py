from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("doctors/", views.doctors_all, name="doctors"),
    path("doctors/<int:id>", views.doctors_more, name="more"),
    path("about/", views.about, name="about"),
]
