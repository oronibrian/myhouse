import django
from django.db import models
import datetime


# Create your models here.


class Vacancy(models.Model):
    housetitle = models.CharField(max_length=250)
    roomsvacant = models.IntegerField()
    housedescription = models.TextField()
    picture = models.ImageField(upload_to='pictures')

    class Meta:
        verbose_name_plural = 'Vacancies'

    def __unicode__(self):
        return self.housetitle


class Booking(models.Model):
    title = models.CharField(max_length=250, default='House Request')
    message = models.TextField(max_length=250, default='')
    email = models.EmailField()
    date = models.DateField(default=django.utils.timezone.now)

    def __unicode__(self):
        return (self.title)
