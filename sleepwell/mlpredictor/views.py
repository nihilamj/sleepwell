from django.shortcuts import render,redirect
import joblib
from django.conf import settings
import os

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
        #print("newdataframe @ viws", data_frame)

        #sleepwell v1 - joblib format

        model_path = os.path.join(settings.BASE_DIR, 'mlpredictor/mlmodels/SleepWellV1.pkl')
        model = joblib.load(model_path)
        predictions = model.predict(data_frame)
        print("Prediction = ", predictions)

        #sleepwell v1 - pkl format

        #sleepwell v2- joblib format
        #sleepwell v2 - pkl format
        
    else:
        return redirect('signin')

