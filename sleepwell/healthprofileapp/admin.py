from django.contrib import admin

# Register your models here.

from .models import HealthProfile, Occupation, HealthRecord

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')

class HealthProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','gender','age','occupation')
    search_fields = ('id','name','email','gender','age','occupation__name')

    @admin.display(ordering='occupation__name',description='occupation name')
    def occupationname(self,obj):
        return obj.occupation.name

class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ('id','healthprofileid','healthprofilename','height','weight','physical_activity','daily_steps','blood_pressure','heart_rate','sleep_duration','quality_of_sleep','stress_level','bmi','sleep_disorder')
    search_fields = ('id','healthprofile__id','healthprofile__name','height','weight','physical_activity','daily_steps','blood_pressure','heart_rate','sleep_duration','quality_of_sleep','stress_level','bmi','sleep_disorder')

    @admin.display(ordering='healthprofile__name',description='healthprofile name')
    def healthprofilename(self,obj):
        return obj.healthprofile.name

    @admin.display(ordering='healthprofile__id',description='healthprofile id')
    def healthprofileid(self,obj):
        return obj.healthprofile.id
    
admin.site.register(HealthProfile,HealthProfileAdmin)
admin.site.register(Occupation,OccupationAdmin)
admin.site.register(HealthRecord,HealthRecordAdmin)