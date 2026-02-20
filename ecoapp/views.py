from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def index(request):
    return render(request,'ecoapp/index.html')

def about_us(request):
    return render(request, 'ecoapp/about_us.html')

def contact_us(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message"),
        )
        return redirect("contact")
    
    return render( request,'ecoapp/contact_us.html')

def services(request):
    return render(request,'ecoapp/services.html')
"""
from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message"),
        )
        return redirect("contact")

    return render(request, "contact.html")
    """