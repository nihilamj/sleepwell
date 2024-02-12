from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import OccupationForm, HealthProfileSignUPForm,HealthProfileSignINForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = HealthProfileSignUPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect to a success URL
        else:
            print("Error")
    else:
        form = HealthProfileSignUPForm()
    
    return render(request, 'healthprofileapp/signup.html', {'page': 'signup','form': form})



def signin(request):
    if request.method == 'POST':
        form = HealthProfileSignINForm(request.POST)
        print("1")
        if form.is_valid():
            return redirect('dashboard')  # Change 'dashboard' to the name of your dashboard URL
    else:
        form = HealthProfileSignINForm()
    return render(request, 'healthprofileapp/signin.html', {'page': 'signin','form': form})



def signout(request):
    logout(request)  # Logout the user
    return redirect('signin')  # Redirect to the sign-in page after logout



def dashboard(request):
    return render(request, 'healthprofileapp/dashboard.html', {'page': 'dashboard'})



