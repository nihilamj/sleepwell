from django.urls import path
from . import views


urlpatterns = [
    

    path("healthrecord_add/", views.healthrecord_add, name="healthrecord_add"),

]