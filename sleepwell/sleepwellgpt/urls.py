from django.urls import path
from . import views


urlpatterns = [
    path("gpt/<int:pk>/", views.chatgpt, name="gpt"),

]