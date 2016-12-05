import datetime

from django.contrib import auth
from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    template = loader.get_template('Homepage/homepage.html')
    context={
        'today': datetime.datetime.now().date(),

    }

    return HttpResponse(template.render(context,request))

def logout(requestt):
    auth.logout(requestt)
    return render_to_response('Homepage/homepage.html')