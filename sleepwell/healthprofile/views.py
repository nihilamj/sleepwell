from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from .models import HealthProfile, Occupation
from .forms import OccupationForm, SignUPForm,SignINForm
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

    messagebox = None

    removeUser(request)

    if request.session.has_key('user_data'):
        del request.session['user_data']

    if request.method == 'POST':
        signup_form = SignUPForm(request.POST)
        try:
            signup_form.is_valid()
            signup_form.save()
            return redirect('signin')  # Redirect to a success URL
        except:
            messagebox = "FORM ERROR, PLEASE CORRECT THE BELOW ERRORS !!!"
    else:
        signup_form = SignUPForm()
    
    return render(request, 'healthprofile/signup.html', {'page': 'signup','signup_form': signup_form,'messagebox':messagebox})



def signin(request):

    messagebox = None

    if request.method == 'POST':
        signin_form = SignINForm(request.POST)

        if signin_form.is_valid():

            removeUser(request)
            try:
                email = signin_form.cleaned_data['email']
                health_profile = HealthProfile.objects.get(email=email)
                
                userrecord = {
                    'id': health_profile.id,
                    'name': health_profile.name,
                    'email': health_profile.email,
                    'password': health_profile.password,
                    'gender': health_profile.gender,
                    'age': health_profile.age,
                    'occupation': health_profile.occupation.name,
                }


                request.session['user_data'] = {'authenticated': True, 'userrecord':userrecord}
            except HealthProfile.DoesNotExist:
                messagebox = "Invalid credentials. Please try again."
            
            return redirect('profile')  # Change 'dashboard' to the name of your dashboard URL
            #return HttpResponseRedirect('/',request)
    else:
        signin_form = SignINForm()
    return render(request, 'healthprofile/signin.html', {'page': 'signin','signin_form': signin_form, 'messagebox':messagebox})



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
