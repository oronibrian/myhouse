from django.db import models

# Create your models here.
class CustomerRequests(models.Model):
    emailadsress = models.EmailField()
    name=models.CharField(max_length=155)
    subject = models.CharField(max_length= 100)
    message =models.CharField(max_length=255)

    def __unicode__(self):
        return self.emailadsress