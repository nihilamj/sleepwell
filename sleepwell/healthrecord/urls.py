from django.urls import path
from . import views


urlpatterns = [
    

    path("healthrecord_view/<int:pk>", views.healthrecord_view, name="healthrecord_view"),
    path("healthrecord_delete/<int:pk>", views.healthrecord_delete, name="healthrecord_delete"),
    path("healthrecord_add/", views.healthrecord_add, name="healthrecord_add"),
    path("healthrecords/", views.healthrecords, name="healthrecords"),
     path('generate_pdf//<int:pk>', views.generate_pdf, name='generate_pdf'),

]