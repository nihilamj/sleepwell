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

        #sleepWellVersion1 - joblib format

        model_path = os.path.join(settings.BASE_DIR, 'mlpredictor/mlmodels/SleepWellVersion1.joblib')
        model = joblib.load(model_path)
        ml_predictions = model.predict(data_frame)
        print("Prediction = ", ml_predictions[0])
        predicted_sleep_disorder = ml_predictions[0]

        #sleepWellVersion1 - pkl format

        #sleepWellVersion2- joblib format
        #sleepWellVersion2 - pkl format
        
        predicted_sleep_disorder = ml_predictions[0]
        healthRecord.sleep_disorder = predicted_sleep_disorder
        healthRecord.save()

        return render(request, 'mlpredictor/report.html', {'page': 'report','healthRecord':healthRecord,'healthProfile':healthProfile})


        
    else:
        return redirect('signin')

