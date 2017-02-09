from django.conf.urls import include, url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.vacancy, name='vacancy'),
    url(r'^sendbooking/$', views.booking, name='sendbooking'),

    url(r'vacancy_api/$', views.VacancyListApiView.as_view(), name='vacancylist'),
    url(r'vacancy_api/(?P<pk>\d+)/$', views.DetailedVacancyDetailApiView.as_view(), name='vacancydetailed'),

    url(r'booking_api/$', views.BookingListApiView.as_view(), name='bookinglist'),
    url(r'booking_api/(?P<pk>\d+)/$', views.DetailedBookingyDetailApiView.as_view(), name='bookingdetailed'),

]
