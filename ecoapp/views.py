from django.shortcuts import render
from django.template import loader
# Create your views here.
def index(request):
    return render(request, 'templates/ecoapp/index.html')

def about_us(request):
    return render(request, 'templates/ecoapp/about_us.html')

def services(request):
    return render(request, 'templates/ecoapp/services.html')

def contact_us(request):
    return render(request, 'templates/ecoapp/contact_us.html')
