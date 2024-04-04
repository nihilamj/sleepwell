import pandas as pd

from healthrecord.models import HealthRecord
from healthprofile.models import HealthProfile


def dataFrame(healthRecord,healthProfile):

     new_data = {}

     new_data = {
          
              'GENDER_FEMALE': [1 if healthProfile.gender == 'FEMALE' else 0],
              'GENDER_MALE': [1 if healthProfile.gender == 'MALE' else 0],
              'GENDER_OTHERS': [1 if healthProfile.gender == 'OTHERS' else 0],

              

              'OCCUPATION_ACCOMMODATION AND FOOD SERVICES': [1 if healthProfile.occupation.name == 'ACCOMMODATION AND FOOD SERVICES' else 0],
              'OCCUPATION_ADMINISTRATIVE AND SUPPORT SERVICES': [1 if healthProfile.occupation.name == 'ADMINISTRATIVE AND SUPPORT SERVICES' else 0],
              'OCCUPATION_AGRICULTURE, FORESTRY, AND FISHING': [1 if healthProfile.occupation.name == 'AGRICULTURE, FORESTRY, AND FISHING' else 0],
              'OCCUPATION_ARTS, ENTERTAINMENT, AND RECREATION': [1 if healthProfile.occupation.name == 'ARTS, ENTERTAINMENT, AND RECREATION' else 0],
              'OCCUPATION_CONSTRUCTION': [1 if healthProfile.occupation.name == 'CONSTRUCTION' else 0],
              'OCCUPATION_CONSULTING': [1 if healthProfile.occupation.name == 'CONSULTING' else 0],
              'OCCUPATION_CUSTOMER SERVICE': [1 if healthProfile.occupation.name == 'CUSTOMER SERVICE' else 0],
              'OCCUPATION_EDUCATIONAL SECTOR': [1 if healthProfile.occupation.name == 'EDUCATIONAL SECTOR' else 0],
              'OCCUPATION_FINANCE AND INSURANCE': [1 if healthProfile.occupation.name == 'FINANCE AND INSURANCE' else 0],
              'OCCUPATION_GOVERNMENT AND PUBLIC ADMINISTRATION': [1 if healthProfile.occupation.name == 'GOVERNMENT AND PUBLIC ADMINISTRATION' else 0],
              'OCCUPATION_HEALTHCARE AND SOCIAL ASSISTANCE': [1 if healthProfile.occupation.name == 'HEALTHCARE AND SOCIAL ASSISTANCE' else 0],
              'OCCUPATION_HOSPITALITY AND TOURISM': [1 if healthProfile.occupation.name == 'HOSPITALITY AND TOURISM' else 0],
              'OCCUPATION_HUMAN RESOURCES': [1 if healthProfile.occupation.name == 'HUMAN RESOURCES' else 0],
              'OCCUPATION_INFORMATION TECHNOLOGY': [1 if healthProfile.occupation.name == 'INFORMATION TECHNOLOGY' else 0],
              'OCCUPATION_LEGAL SERVICES': [1 if healthProfile.occupation.name == 'LEGAL SERVICES' else 0],
              'OCCUPATION_MANUFACTURING': [1 if healthProfile.occupation.name == 'MANUFACTURING' else 0],
              'OCCUPATION_MARKETING AND ADVERTISING': [1 if healthProfile.occupation.name == 'MARKETING AND ADVERTISING' else 0],
              'OCCUPATION_MEDIA AND COMMUNICATIONS': [1 if healthProfile.occupation.name == 'MEDIA AND COMMUNICATIONS' else 0],
              'OCCUPATION_MINING, QUARRYING, AND OIL AND GAS EXTRACTION' : [1 if healthProfile.occupation.name == 'MINING, QUARRYING, AND OIL AND GAS EXTRACTION' else 0],
              'OCCUPATION_NONPROFIT ORGANIZATIONS': [1 if healthProfile.occupation.name == 'NONPROFIT ORGANIZATIONS' else 0] ,
              'OCCUPATION_OTHERS': [1 if healthProfile.occupation.name == 'OTHERS' else 0],
              'OCCUPATION_PROFESSIONAL, SCIENTIFIC, AND TECHNICAL SERVICES': [1 if healthProfile.occupation.name == 'PROFESSIONAL, SCIENTIFIC, AND TECHNICAL SERVICES' else 0],
              'OCCUPATION_REAL ESTATE AND RENTAL AND LEASING': [1 if healthProfile.occupation.name == 'REAL ESTATE AND RENTAL AND LEASING' else 0],
              'OCCUPATION_RESEARCH AND DEVELOPMENT': [1 if healthProfile.occupation.name == 'RESEARCH AND DEVELOPMENT' else 0],
              'OCCUPATION_RETAIL TRADE': [1 if healthProfile.occupation.name == 'RETAIL TRADE' else 0],
              'OCCUPATION_SALES AND BUSINESS DEVELOPMENT': [1 if healthProfile.occupation.name == 'SALES AND BUSINESS DEVELOPMENT' else 0],
              'OCCUPATION_TRANSPORTATION AND WAREHOUSING': [1 if healthProfile.occupation.name == 'TRANSPORTATION AND WAREHOUSING' else 0],
              'OCCUPATION_UTILITIES': [1 if healthProfile.occupation.name == 'UTILITIES' else 0],
              'OCCUPATION_WASTE MANAGEMENT AND REMEDIATION SERVICES': [1 if healthProfile.occupation.name == 'WASTE MANAGEMENT AND REMEDIATION SERVICES' else 0],
              'OCCUPATION_WHOLESALE TRADE': [1 if healthProfile.occupation.name == 'WHOLESALE TRADE' else 0],

              'AGE': [healthProfile.age],
              
              'PHYSICAL_ACTIVITY': [healthRecord.physical_activity], # Value in Minute

              'SCREEN_TIME': [healthRecord.screen_time], # Value in Minute

              'STRESS_LEVEL': [healthRecord.stress_level], # Range 1 to 10

              'HEART_RATE': [healthRecord.heart_rate], # BPM

              'SYSTOLIC_PRESSURE': [healthRecord.systolic_pressure], #mm Hg
              'DIASTOLIC_PRESSURE': [healthRecord.diastolic_pressure], #mm Hg

              'HEIGHT': [healthRecord.height], # centimeter
              'WEIGHT': [healthRecord.weight], #Kilogram

              'SLEEP_DURATION': [healthRecord.sleep_duration], # Value in Minute

              'QUALITY_OF_SLEEP': [healthRecord.quality_of_sleep] # Range 1 to 10

     }

     newdataframe = pd.DataFrame(new_data)

     print("newdataframe", newdataframe)
     
     return newdataframe