from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html', {'page': 'home'})

def about(request):
    return render(request, 'mainapp/about.html', {'page': 'about'})