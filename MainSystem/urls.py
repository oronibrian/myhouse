
from django.conf.urls import include, url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'bulding_api/$', views.BuildinListApiView.as_view(), name='buidinglist'),
    url(r'bulding_api/(?P<pk>\d+)/$', views.DetailedBuildingApiView.as_view(), name='buidingdetailed'),

    url(r'property_api/$', views.PropertyListApiView.as_view(), name='propertylist'),
    url(r'property_api/(?P<pk>\d+)/$', views.DetailedPropertyApiView.as_view(), name='propertydetailed'),

    url(r'tenant_api/$', views.TenantListApiView.as_view(), name='tenantlist'),
    url(r'tenant_api/(?P<pk>\d+)/$', views.DetailedTenantApiView.as_view(), name='tenetdetailed'),

]
