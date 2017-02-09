
from django.conf.urls import include, url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.ContactUs, name='contactus'),
    url(r'^sendrequest/$', views.SendRequest, name='sendrequest'),

]
