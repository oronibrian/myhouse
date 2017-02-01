import datetime

from django.contrib import auth
from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse
from django.core.mail import mail_admins
from rest_framework.generics import RetrieveAPIView, ListAPIView

from MainSystem.AllSerializers import BuildingSerializer, PropertySerializer, TenantSerializer
from .models import Building, Property, Tenant

# Create your views here.
from MainSystem.models import Building


def index(request):
    template = loader.get_template('Homepage/homepage.html')
    context={
        'today': datetime.datetime.now().date(),

    }

    return HttpResponse(template.render(context,request))

def logout(request):
    auth.logout(request)
    return render_to_response('Homepage/homepage.html')


def register(request):
    template = loader.get_template('registration/registeruser.html')
    context = {
        'today': datetime.datetime.now().date(),

    }

    return HttpResponse(template.render(context, request))



#this is for the api view of all building data
class BuildinListApiView(ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class DetailedBuildingApiView(RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer



#this is for the api view of all Property data
class PropertyListApiView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class DetailedPropertyApiView(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

#this is for the api view of all Tenant data
class TenantListApiView(ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class DetailedTenantApiView(RetrieveAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer