from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class   TenantProfile(models.Model):
     user = models.OneToOneField(User)
     fullname = models.CharField(max_length=155)
     email = models.EmailField()


User.profile = property(lambda u:TenantProfile.objects.get_or_create(user=u)[0])