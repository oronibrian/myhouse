from django.conf.urls import include, url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.vacancy, name='vacancy'),
    url(r'^sendbooking/$', views.booking, name='sendbooking')

]
