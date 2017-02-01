import django
from django.core.mail import mail_admins
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from Vacancy.models import Vacancy
import datetime
from .forms import BookingForm


# Create your views here.

def vacancy(request):
    template = loader.get_template('Vacancy/vacancy.html')
    result = []
    vacancy = (Vacancy.objects.all())

    context = {
        'today': datetime.datetime.now().date(),
        'vacancies': vacancy
    }

    return HttpResponse(template.render(context, request))


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            post = form.save(commit='False')
            post.published_date = django.utils.timezone.now
            post.save()
            return redirect('vacancy')
    else:

        form = BookingForm()

    return render(request, 'Vacancy/booking.html', {'form': form})
