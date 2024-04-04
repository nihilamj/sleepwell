from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from .models import HealthRecord
from healthprofile.models import HealthProfile

# Create your views here.
def healthrecord_add(request):

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
        if request.method == 'POST':
            
            healthprofile = HealthProfile.objects.get(id=data['userrecord']['id'])
            height = int(request.POST.get('height'))
            weight = int(request.POST.get('weight'))
            physical_activity = int(request.POST.get('physical_activity'))
            screen_time = int(request.POST.get('screen_time'))
            stress_level = int(request.POST.get('stress_level'))
            heart_rate = int(request.POST.get('heart_rate'))
            systolic_pressure = int(request.POST.get('systolic_pressure'))
            diastolic_pressure = int(request.POST.get('diastolic_pressure'))
            sleep_duration = int(request.POST.get('sleep_duration'))
            quality_of_sleep = int(request.POST.get('quality_of_sleep'))
            healthrecord =  HealthRecord.objects.create(healthprofile=healthprofile,height=height,weight=weight,physical_activity=physical_activity,screen_time=screen_time,stress_level=stress_level,heart_rate=heart_rate,systolic_pressure=systolic_pressure,diastolic_pressure=diastolic_pressure,sleep_duration=sleep_duration,quality_of_sleep=quality_of_sleep)

            print(healthrecord)
            return render(request, 'healthrecord/healthrecord_add.html', {'page': 'healthrecord_add','data':data})
        else:
            return render(request, 'healthrecord/healthrecord_add.html', {'page': 'healthrecord_add','data':data})
    else:
        return redirect('signin')
