from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

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

            messages.info(request, "New HealthRecord Added successfully")
            return render(request, 'healthrecord/healthrecord_add.html', {'page': 'healthrecord_add','data':data})
        else:
            return render(request, 'healthrecord/healthrecord_add.html', {'page': 'healthrecord_add','data':data})
    else:
        return redirect('signin')


def healthrecord_view(request,pk):

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

        
        try:
            # health_profile_id = data['userrecord']['id']
            # HealthProfile.objects.get(pk=)
            health_record = HealthRecord.objects.get(pk=pk,healthprofile=data['userrecord']['id'])

            data ={
                'healthrecord':health_record
            }
                       
            return render(request, 'healthrecord/healthrecord_view.html', {'page': 'healthrecord_view','data':data})
        except:
            messages.error(request,'No Health Record for the id')
    else:
        return redirect('signin')


def healthrecord_delete(request,pk):

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

        
        try:
            # health_profile_id = data['userrecord']['id']
            # HealthProfile.objects.get(pk=)
            health_record = HealthRecord.objects.get(pk=pk,healthprofile=data['userrecord']['id'])

            try:
                health_record = HealthRecord.objects.get(pk=pk, healthprofile=data['userrecord']['id'])
                health_record.delete()
                messages.success(request,"Record deleted successfully")
                return redirect('healthrecords')
            except HealthRecord.profile:
                messages.error(request,"Record does not exist")
                return redirect('healthrecords')
            except Exception as e:
                messages.error(request,"An error occurred:"+ str(e))
                return redirect('healthrecords')
                
                       
            return render(request, 'healthrecord/healthrecord_view.html', {'page': 'healthrecord_view','data':data})
        except:
            messages.error(request,'No Health Record for the id')
            return redirect('profile')
    else:
        return redirect('signin')

def healthrecords(request):

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

        
        try:
            # health_profile_id = data['userrecord']['id']
            # HealthProfile.objects.get(pk=)
            
            health_profile = HealthProfile.objects.get(pk=data['userrecord']['id'])
            health_records = HealthRecord.objects.filter(healthprofile=health_profile)
            print("1")
            print(health_records)

            data ={
                'healthrecords':health_records
            }
                       
            return render(request, 'healthrecord/healthrecords.html', {'page': 'healthrecords','data':data})
        except Exception as e:
            print("An error occurred:", e)
            messages.error(request, 'An error occurred while fetching health records.')
            return redirect('profile')
    else:
        return redirect('signin')