from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("", views.profile, name="profile"),

    path("healthrecord_add/", views.healthrecord_add, name="healthrecord_add"),

    path('signout/', views.signout, name='signout'),
]