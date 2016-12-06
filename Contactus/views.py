from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime
from MainSystem.models import CompanyDetail
# Create your views here.
def ContactUs(request):
   template = loader.get_template('Contactus/contactus.html')
   for instance in CompanyDetail.objects.all():
       name= instance.companyname

   context = {
        'companyname':name,
        'address': instance.address,
        'email': instance.emailaddress,
        'contact': instance.staffcontact,
       'admincontact':instance.admincontact,
       'ownercontact':instance.ownercontact,
        'town':instance.town,

        'today': datetime.datetime.now().date(),

   }

   return HttpResponse(template.render(context, request))