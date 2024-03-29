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
        x=['GENDER_FEMALE', 'GENDER_MALE', 'GENDER_OTHERS',
       'OCCUPATION_ACCOMMODATION AND FOOD SERVICES',
       'OCCUPATION_ADMINISTRATIVE AND SUPPORT SERVICES',
       'OCCUPATION_AGRICULTURE, FORESTRY, AND FISHING',
       'OCCUPATION_ARTS, ENTERTAINMENT, AND RECREATION',
       'OCCUPATION_CONSTRUCTION', 'OCCUPATION_CONSULTING',
       'OCCUPATION_CUSTOMER SERVICE', 'OCCUPATION_EDUCATIONAL SECTOR',
       'OCCUPATION_FINANCE AND INSURANCE',
       'OCCUPATION_GOVERNMENT AND PUBLIC ADMINISTRATION',
       'OCCUPATION_HEALTHCARE AND SOCIAL ASSISTANCE',
       'OCCUPATION_HOSPITALITY AND TOURISM', 'OCCUPATION_HUMAN RESOURCES',
       'OCCUPATION_INFORMATION TECHNOLOGY', 'OCCUPATION_LEGAL SERVICES',
       'OCCUPATION_MANUFACTURING', 'OCCUPATION_MARKETING AND ADVERTISING',
       'OCCUPATION_MEDIA AND COMMUNICATIONS',
       'OCCUPATION_MINING, QUARRYING, AND OIL AND GAS EXTRACTION',
       'OCCUPATION_NONPROFIT ORGANIZATIONS', 'OCCUPATION_OTHERS',
       'OCCUPATION_PROFESSIONAL, SCIENTIFIC, AND TECHNICAL SERVICES',
       'OCCUPATION_REAL ESTATE AND RENTAL AND LEASING',
       'OCCUPATION_RESEARCH AND DEVELOPMENT', 'OCCUPATION_RETAIL TRADE',
       'OCCUPATION_SALES AND BUSINESS DEVELOPMENT',
       'OCCUPATION_TRANSPORTATION AND WAREHOUSING', 'OCCUPATION_UTILITIES',
       'OCCUPATION_WASTE MANAGEMENT AND REMEDIATION SERVICES',
       'OCCUPATION_WHOLESALE TRADE', 'AGE', 'PHYSICAL_ACTIVITY', 'SCREEN_TIME',
       'STRESS_LEVEL', 'HEART_RATE', 'SYSTOLIC_PRESSURE', 'DIASTOLIC_PRESSURE',
       'HEIGHT', 'WEIGHT', 'SLEEP_DURATION', 'QUALITY_OF_SLEEP']
        #print("newdataframe @ viws", data_frame)

        #sleepwell v1 - joblib format

        model_path = os.path.join(settings.BASE_DIR, 'mlpredictor/mlmodels/SleepWellV1.pkl')
        model = joblib.load(model_path)
        predictions = model.predict(data_frame[x])
        print("Prediction = ", predictions)

        #sleepwell v1 - pkl format

        #sleepwell v2- joblib format
        #sleepwell v2 - pkl format
        
    else:
        return redirect('signin')

