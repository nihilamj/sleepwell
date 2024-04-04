from django.shortcuts import render, redirect
import openai
import jinja2

from healthrecord.models import HealthRecord
from healthprofile.models import HealthProfile

from sleepwell import settings

# Create your views here.

def chatgpt(request, pk):

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

        prompt = """ 
        
            The user has provided the following attributes and values:

            AGE: """+str(healthProfile.age)+"""
            GENDER: """+healthProfile.gender+"""
            OCCUPATION SECTOR: """+healthProfile.occupation.name+"""
            HEIGHT: """+str(healthRecord.height)+""" CM
            WEIGHT: """+str(healthRecord.weight)+""" KG
            BMI VALUE: """+str(healthRecord.bmi_value)+"""
            BMI: """+str(healthRecord.bmi)+"""
            SYSTOLIC PRESSURE: """+str(healthRecord.systolic_pressure)+""" mmHg
            SYSTOLIC PRESSURE CATEGORY: """+healthRecord.systolic_pressure_bp+"""
            DIASTOLIC PRESSURE: """+str(healthRecord.systolic_pressure)+""" mmHg
            DIASTOLIC PRESSURE CATEGORY: """+healthRecord.diastolic_pressure_bp+"""
            PHYSICAL ACTIVITY: """+str(healthRecord.physical_activity)+""" Minutes
            SCREEN TIME: """+str(healthRecord.screen_time)+""" Minutes
            STRESS LEVEL: """+str(healthRecord.stress_level)+""" out of 10
            HEART RATE: """+str(healthRecord.heart_rate)+""" BPM
            SLEEP DURATION: """+str(healthRecord.sleep_duration)+""" Minutes
            QUALITY OF SLEEP: """+str(healthRecord.quality_of_sleep)+""" out of 10
            SLEEP DISORDER: """+healthRecord.sleep_disorder+"""
        
            Based on these attributes, create a personalized, healthy, step-by-step health plan. This plan should include recommendations for sleep schedule, exercises, food habits, lifestyle adjustments, do's and don'ts, and areas of focus or improvement. Ensure that the plan addresses the user's current health status and compares it with ideal or optimum values for each attribute. Provide detailed instructions for each aspect of the plan to help the user achieve better health outcomes.
        """
        print(prompt)

        
        client = openai.OpenAI(
            # This is the default and can be omitted
            api_key = settings.OPENAI_API_KEY
        )

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                    
                }
            ],
            model="gpt-3.5-turbo",
        )
        
        print(response)
        chatgpt_response = response.choices[0].message.content.strip()
        #html_response = chatgpt_response.replace('\n', '<br>')
        # html_response = jinja2.Template(chatgpt_response.replace('\n', '<br>')).render()
        html_response = chatgpt_response.split('\n')
        return render(request, 'sleepwellgpt/healthplan.html', {'page': 'healthplan','html_response': html_response})
        
    else:
            return redirect('signin')
    


def generate_personalized_health_plan(user_data):
    # Generate personalized health plan based on user data
    # Example implementation:
    health_plan = ""
    # Include recommendations based on user's health status
    # Example: health_plan += "Recommendations for improving sleep: ..."
    return health_plan

