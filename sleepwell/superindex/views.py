from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'superindex/home.html', {'page': 'home'})

def about(request):
    return render(request, 'superindex/about.html', {'page': 'about'})

def healthy_lifestyle(request):
    return render(request, 'superindex/healthy_lifestyle.html', {'page': 'healthy_lifestyle'})