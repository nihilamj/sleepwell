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

def getOTPsession(request):
    if request.session.has_key('one_time_password'):
        return request.session['one_time_password']

def createOTPsession(request):
    request.session['one_time_password'] = {}
    return request.session['one_time_password']

def removeOTPsession(request):
    if request.session.has_key('one_time_password'):
        del request.session['one_time_password']

# Create your views here.

def signup(request):

    
    
    removeUser(request)
    removeOTPsession(request)

    if request.method == 'POST':
        signup_form = SignUPForm(request.POST)
        try:
            signup_form.is_valid()
            signup_form.save()
            messages.success(request, "Health Profile created successfully!!!")
            return redirect('signin')  # Redirect to a success URL
        except:
            
            messages.error(request, "OOPS!! Form error")
    else:
        signup_form = SignUPForm()
    
    return render(request, 'healthprofile/signup.html', {'page': 'signup','signup_form': signup_form})



def signin(request):

    removeUser(request)
    removeOTPsession(request)

    

    if request.method == 'POST':
        signin_form = SignINForm(request.POST)

        if signin_form.is_valid():

            

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
                    'is_active':health_profile.is_active
                }


                
            except HealthProfile.DoesNotExist:
                
                messages.error(request, "OOPS!! Error")

            if health_profile.is_active:
                request.session['user_data'] = {'authenticated': True, 'userrecord':userrecord}
                return redirect('profile')  # Change 'dashboard' to the name of your dashboard URL
            else:
                messages.warning(request, "Your account isn't activated")
                messages.info(request, "Please Activate your account")
                otp_session = createOTPsession(request)
                otp_session['stage'] = 'activation'
                request.session['one_time_password'] = otp_session
                return redirect('generateotp')
            
    else:
        signin_form = SignINForm()
    return render(request, 'healthprofile/signin.html', {'page': 'signin','signin_form': signin_form})



def signout(request):
    removeUser(request)
    removeOTPsession(request)
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

    removeUser(request)

    try:
        otp_session = getOTPsession(request)
    except:
        return redirect('/')

    if request.method == 'POST':
        email = request.POST.get('email')
        userrecord = HealthProfile.objects.get(email=email)
        pk = userrecord.pk
        if userrecord:
            otp = otp_generate()
            messages.info(request, "An OTP has sent to your email")
            # request.session['passwordreset']={'pk':pk, 'otp':otp}

            otp_session['pk'] = pk
            otp_session['otp'] = otp
            request.session['one_time_password'] = otp_session

            otpmail(email=email, otp=otp, stage = request.session['one_time_password'].get('stage', None))

            return redirect('otp_verification')  

        else:
            pass # return no user found for this email
    
    return render(request, 'healthprofile/generateotp.html', {'page': 'generateotp'})

def otp_verification(request):
    if request.session.has_key('one_time_password'):

        if request.method == 'POST':
            entered_otp = request.POST.get('otp')

            if entered_otp == request.session['one_time_password'].get('otp', None) and request.session['one_time_password'].get('stage', None) == 'reset_password':
                # OTP verification successful, allow user to reset password
                return redirect('reset_password')
            
            elif entered_otp == request.session['one_time_password'].get('otp', None) and request.session['one_time_password'].get('stage', None) == 'activation':
                return redirect('account_activation')

            else:
                # Incorrect OTP entered
                messages.error(request, "OOPS!! OTP is wrong")
                return render(request, 'healthprofile/otp_verification.html')
            
        return render(request, 'healthprofile/otp_verification.html')
    else:
        return redirect('generateotp')
    


def reset_forgot_password(request):
    otp_session = createOTPsession(request)
    otp_session['stage'] = 'reset_password'
    request.session['one_time_password'] = otp_session
    return redirect('generateotp')

def reset_password(request):
    if request.session.has_key('otp'):
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

def account_activation(request):
    otp_session = getOTPsession(request)
    pk = otp_session.get('pk')
    userrecord = HealthProfile.objects.get(pk=pk)
    userrecord.is_active = True
    userrecord.save()
    return redirect('signin')