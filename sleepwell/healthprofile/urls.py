from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path('signout/', views.signout, name='signout'),
    
    path("", views.profile, name="profile"),


    path('generateotp/', views.generateotp, name='generateotp'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('reset_forgot_password/', views.reset_forgot_password, name='reset_forgot_password'),
    path('account_activation/', views.account_activation, name='account_activation'),
]