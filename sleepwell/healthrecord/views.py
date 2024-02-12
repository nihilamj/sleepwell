from django.shortcuts import render,redirect
from .forms import OccupationForm, HealthProfileSignUPForm

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
    
    return render(request, 'healthrecord/signup.html', {'page': 'signup','form': form})


def signin(request):
    return render(request, 'healthrecord/signin.html', {'page': 'signin'})