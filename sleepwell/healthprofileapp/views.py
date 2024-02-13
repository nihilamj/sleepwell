from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import OccupationForm, HealthProfileSignUPForm,HealthProfileSignINForm
from django.contrib import messages

# Basic Functions

def getUser(request):
    if request.session.has_key('user_data'):
        return request.session['user_data']


def removeUser(request):
    if request.session.has_key('user_data'):
        del request.session['user_data']

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
            removeUser(request)
            request.session['user_data'] = {'authenticated': True}
            return redirect('dashboard')  # Change 'dashboard' to the name of your dashboard URL
            #return HttpResponseRedirect('/',request)
    else:
        form = HealthProfileSignINForm()
    return render(request, 'healthprofileapp/signin.html', {'page': 'signin','form': form})



def signout(request):
    if request.session.has_key('user_data'):
        del request.session['user_data']
    return redirect('signin')  # Redirect to the sign-in page after logout
    



def dashboard(request):
    
    data = {}

    if 'user_data' in request.session:
        if request.session['user_data'] is not None:
            data['authenticated'] = request.session['user_data'].get('authenticated', False)
        else:
            # Handle the case where request.session['user_data'] is None
            # For example, set data['authenticated'] to False or another default value
            data['authenticated'] = False
    else:
        # Handle the case where 'user_data' doesn't exist in request.session
        # For example, set data['authenticated'] to False or another default value
        data['authenticated'] = False
    
    return render(request, 'healthprofileapp/dashboard.html', {'page': 'dashboard','data':data})



