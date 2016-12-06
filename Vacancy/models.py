from django.db import models

# Create your models here.
class Vacancy(models.Model):
    housetitle=models.CharField(max_length=250)
    roomsvacant = models.IntegerField()
    housedescription=models.TextField()
    class Meta:
        verbose_name_plural='Vacancies'

    def __unicode__(self):
        return self.housetitle

