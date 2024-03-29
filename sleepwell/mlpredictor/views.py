from django.shortcuts import render,redirect

from healthprofileapp.models import HealthRecord,HealthProfile

from .newdataframe import dataFrame

def predict(request,pk):

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

        healthRecord = HealthRecord.objects.get(pk=pk)
        healthProfile = HealthProfile.objects.get(pk=healthRecord.healthprofile.id)

        data_frame = dataFrame(healthRecord,healthProfile)

        print("newdataframe @ viws", data_frame)
        
    else:
        return redirect('signin')

