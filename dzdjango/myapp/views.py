from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Главная страница</h1>")
def data(request):
    return HttpResponse("<h1>Страница данных</h1>")

def test(request):
    return HttpResponse("<h1>Тестовая страница</h1>")