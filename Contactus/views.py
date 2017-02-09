from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime

from Contactus.models import CustomerRequests
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


def SendRequest(request):
    if request.method=='POST':
        email= request.POST['email']
        name= request.POST['name']
        subject= request.POST['subject']
        message = request.POST['message']

        CustomerRequests.objects.create(
            email=email,
            name =name,
            subject=subject,
            message = message

        )

        return HttpResponse("")