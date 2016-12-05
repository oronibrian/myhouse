
from django.conf.urls import include, url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.tenant, name='tenant'),
    #url(r'^tenant/(?P<tenant_id>\d+)/$', views.tenant, name="tenant"),

]
