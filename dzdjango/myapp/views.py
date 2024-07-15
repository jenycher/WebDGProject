from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def data(request):
    return render(request, 'data.html')

def test(request):
    return render(request, 'test.html')
