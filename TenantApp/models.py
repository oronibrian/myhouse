from django.db import models

# Create your models here.
class MovingInInstructions(models.Model):
    instruction = models.TextField()


    def __unicode__(self):              # __unicode__ on Python 2

        return self.instruction


class MovingOutInstructions(models.Model):
    instruction = models.TextField()

    def __unicode__(self):  # __unicode__ on Python 2
        return self.instruction