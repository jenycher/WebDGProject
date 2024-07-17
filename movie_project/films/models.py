from django.db import models

# Create your models here.
#название фильма, поле для описание фильма и поле для отзыва.

class films(models.Model):
    title = models.CharField('Название фильма', max_length=100)
    description = models.CharField('Описание фильма', max_length=200)
    review = models.TextField('Отзыв')


