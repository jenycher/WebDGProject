from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.film_create_view, name='film_create'),
    path('list/', views.film_list_view, name='film_list'),
]
