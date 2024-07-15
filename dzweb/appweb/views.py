from django.shortcuts import render

# Create your views here.
# appweb/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'appweb/home.html')

def about(request):
    return render(request, 'appweb/about.html')

def services(request):
    return render(request, 'appweb/services.html')

def contact(request):
    return render(request, 'appweb/contact.html')
