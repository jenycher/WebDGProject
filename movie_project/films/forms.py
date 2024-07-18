from django import forms
from .models import Film
from django.forms import ModelForm, TextInput, Textarea

class FilmForm(forms.ModelForm):
	class Meta:
		model = Film
		fields = ['title', 'description', 'review']
		widgets = {
			'title': TextInput(attrs={'class': 'form-contrl', 'placeholder': 'Название фильма'}),
			'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
			'review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),
			}

