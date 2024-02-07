from django.contrib import admin

# Register your models here.

from .models import HealthProfile, Occupation

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')

class HealthProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','gender','age','occupations')
    search_fields = ('id','name','email','gender','age','occupations__name')

    @admin.display(ordering='occupations__name',description='occupations name')
    def occupationname(self,obj):
        return obj.occupation.name

admin.site.register(HealthProfile,HealthProfileAdmin)
admin.site.register(Occupation,OccupationAdmin)
