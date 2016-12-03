from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime

# Create your views here.
@login_required
def tenant(request):
    template = loader.get_template('TenantApp/tenant.html')
    context = {
        'today': datetime.datetime.now().date(),

    }

    return HttpResponse(template.render(context, request))