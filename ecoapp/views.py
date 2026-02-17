from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'ecoapp/index.html')

def about_us(request):
    return render(request, 'ecoapp/about_us.html')

def contact_us(request):
    return render(request,'ecoapp/contact_us.html')

def services(request):
    return render(request,'ecoapp/services.html')