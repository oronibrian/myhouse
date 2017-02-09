from django.db import models

# Create your models here.
class CustomerRequests(models.Model):
    email = models.EmailField()
    name=models.CharField(max_length=155)
    subject = models.CharField(max_length= 100)
    message =models.TextField  (max_length=255)

    def __unicode__(self):
        return (self.subject)