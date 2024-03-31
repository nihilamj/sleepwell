from django.urls import path
from . import views


urlpatterns = [
    path("chatgpt/<int:pk>/", views.chatgpt, name="chatgpt"),

]