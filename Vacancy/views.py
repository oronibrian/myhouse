from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from Vacancy.models import Vacancy
import datetime

# Create your views here.

def vacancy(request):
    template = loader.get_template('Vacancy/vacancy.html')
    result = []
    vacancy = (Vacancy.objects.all())

    context = {
        'today': datetime.datetime.now().date(),
        'vacancies':vacancy
    }

    return HttpResponse(template.render(context, request))