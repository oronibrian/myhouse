import django
from django.core.mail import mail_admins
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView

from Vacancy.models import Vacancy, Booking
import datetime

from Vacancy.vacancyserializer import VacancySerializer, BookingSerializer
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


# this is for the api view of all Vacancy details data
class VacancyListApiView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class DetailedVacancyDetailApiView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


# this is for the api view of all Booking details data
class BookingListApiView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class DetailedBookingyDetailApiView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
