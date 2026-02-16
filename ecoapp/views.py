from django.shortcuts import render
from django.template import loader
# Create your views here.
def index(request):
    return render(request,template_name='index.html')

def about_us(request):
    return render(request, 'about_us.html')


def contact_us(request):
    return render(request,template_name='contact_us.html')


def services(request):
    return render(request,template_name='services.html')