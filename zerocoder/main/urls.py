from django.urls import path
from django.urls import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2')
]