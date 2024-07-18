from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    description = models.CharField('Описание фильма', max_length=200)
    review = models.TextField('Отзыв')

    def __str__(self):
        return self.title


