from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("", views.profile, name="profile"),

    path("healthrecord_add/", views.healthrecord_add, name="healthrecord_add"),

    path('signout/', views.signout, name='signout'),

    path('generateotp/', views.generateotp, name='generateotp'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('reset_password/', views.reset_password, name='reset_password'),
]