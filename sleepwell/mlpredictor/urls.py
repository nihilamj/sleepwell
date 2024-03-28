from django.urls import path
from . import views


urlpatterns = [
    path("predict/<int:pk>/", views.predict, name="predict"),
    
]