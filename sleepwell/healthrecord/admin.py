from django.contrib import admin

# Register your models here.

from healthprofile.models import HealthProfile, Occupation
from .models import HealthRecord

class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ('id','healthprofileid','healthprofilename','height','weight','bmi_value','bmi','physical_activity','screen_time','stress_level','heart_rate','systolic_pressure','systolic_pressure_bp','diastolic_pressure','diastolic_pressure_bp','sleep_duration','quality_of_sleep','sleep_disorder','created_at')
    search_fields = ('id','healthprofile__id','healthprofile__name','height','weight','bmi_value','bmi','physical_activity','screen_time','stress_level','heart_rate','systolic_pressure','systolic_pressure_bp','diastolic_pressure','diastolic_pressure_bp','sleep_duration','quality_of_sleep','sleep_disorder','created_at')

    @admin.display(ordering='healthprofile__name',description='healthprofile name')
    def healthprofilename(self,obj):
        return obj.healthprofile.name

    @admin.display(ordering='healthprofile__id',description='healthprofile id')
    def healthprofileid(self,obj):
        return obj.healthprofile.id
    

admin.site.register(HealthRecord,HealthRecordAdmin)