from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("healthy_lifestyle/", views.healthy_lifestyle, name="healthy_lifestyle"),
]