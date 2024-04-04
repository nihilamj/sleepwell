from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from .models import HealthProfile, Occupation
from .forms import OccupationForm, HealthProfileSignUPForm,HealthProfileSignINForm
from django.contrib import messages

from .mails import otpmail


from .otpgenerate import otp_generate


def getUser(request):
    if request.session.has_key('user_data'):
        return request.session['user_data']


def removeUser(request):
    if request.session.has_key('user_data'):
        del request.session['user_data']

# Create your views here.

def signup(request):
    removeUser(request)
    if request.session.has_key('user_data'):
        del request.session['user_data']
    if request.method == 'POST':
        form = HealthProfileSignUPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect to a success URL
        else:
            print("Error")
    else:
        form = HealthProfileSignUPForm()
    
    return render(request, 'healthprofile/signup.html', {'page': 'signup','form': form})



def signin(request):

    if request.method == 'POST':
        form = HealthProfileSignINForm(request.POST)
        print("1")
        if form.is_valid():
            removeUser(request)
            try:
                email = form.cleaned_data['email']
                health_profile = HealthProfile.objects.get(email=email)
                
                print(health_profile)
                userrecord = {
                    'id': health_profile.id,
                    'name': health_profile.name,
                    'email': health_profile.email,
                    'password': health_profile.password,
                    'gender': health_profile.gender,
                    'age': health_profile.age,
                    'occupation': health_profile.occupation.name,
                }

                print(userrecord)
                request.session['user_data'] = {'authenticated': True, 'userrecord':userrecord}
            except HealthProfile.DoesNotExist:
                return HTTPResponse("Invalid credentials. Please try again.")
            
            return redirect('profile')  # Change 'dashboard' to the name of your dashboard URL
            #return HttpResponseRedirect('/',request)
    else:
        form = HealthProfileSignINForm()
    return render(request, 'healthprofile/signin.html', {'page': 'signin','form': form})



def signout(request):
    if request.session.has_key('user_data'):
        del request.session['user_data']
    return redirect('signin')  # Redirect to the sign-in page after logout
    



def profile(request):
    
    data = {}

    if 'user_data' in request.session:
        if request.session['user_data'] is not None:
            #Here add the code fetch data from session
            data['authenticated'] = request.session['user_data'].get('authenticated', False)
            data['userrecord'] = request.session['user_data'].get('userrecord')
        else:
            # Handle the case where request.session['user_data'] is None
            # For example, set data['authenticated'] to False or another default value
            data['authenticated'] = False
    else:
        # Handle the case where 'user_data' doesn't exist in request.session
        # For example, set data['authenticated'] to False or another default value
        data['authenticated'] = False
        
    if data['authenticated']:
        return render(request, 'healthprofile/profile.html', {'page': 'profile','data':data})
    else:
        return redirect('signin')
    


def generateotp(request):
    if request.session.has_key('user_data'):
        del request.session['user_data']

    if request.method == 'POST':
        email = request.POST.get('email')
        userrecord = HealthProfile.objects.get(email=email)
        pk = userrecord.pk
        if userrecord:
            otp = otp_generate()
            request.session['passwordreset']={'pk':pk, 'otp':otp}
            otpmail(email=email, otp=otp)
            return redirect('otp_verification')  

        else:
            pass # return no user found for this email
    
    return render(request, 'healthprofile/generateotp.html', {'page': 'generateotp'})

def otp_verification(request):
    if request.session.has_key('passwordreset'):
        if request.method == 'POST':
            entered_otp = request.POST.get('otp')
            if entered_otp == request.session['passwordreset'].get('otp', False):
                # OTP verification successful, allow user to reset password
                return redirect('reset_password')
            else:
                # Incorrect OTP entered
                return render(request, 'healthprofile/otp_verification.html', {'error': 'Invalid OTP'})
            
        return render(request, 'healthprofile/otp_verification.html')
    else:
        return redirect('generateotp')

def reset_password(request):
    if request.session.has_key('passwordreset'):
        if request.method == 'POST':
            password = request.POST.get('password')
            pk = request.session['passwordreset'].get('pk', None)
            userrecord = HealthProfile.objects.get(pk=pk)
            userrecord.password=password
            userrecord.save()
            return redirect('signin')
        return render(request, 'healthprofile/reset_password.html')
    else:
        return redirect('generateotp')
