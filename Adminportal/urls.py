from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.tenants, name="tenants"),
    url(r'^tenant-cashflows/(?P<tenant_id>\d+)/$',views.tenant_cashflows, name="tenant_cashflows"),
    url(r'^invoice/',views.invoice,name="invoice"),
    url(r'^myinvoice/$',views.Myinvoice,name="myinvoice"),

)
