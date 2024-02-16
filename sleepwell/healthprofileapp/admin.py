from django.contrib import admin

# Register your models here.

from .models import HealthProfile, Occupation

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')

class HealthProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','gender','age','occupation')
    search_fields = ('id','name','email','gender','age','occupation__name')

    @admin.display(ordering='occupation__name',description='occupation name')
    def occupationname(self,obj):
        return obj.occupation.name

admin.site.register(HealthProfile,HealthProfileAdmin)
admin.site.register(Occupation,OccupationAdmin)