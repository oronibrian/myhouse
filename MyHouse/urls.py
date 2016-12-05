from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import logout
from django.views.generic import RedirectView
from MainSystem import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='homepage/', permanent=True)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homepage/', include('MainSystem.urls')),
    url(r'^tenant/' ,include('TenantApp.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', views.logout),
    url(r'^contactus/',include('Contactus.urls')),
    url(r'^vacancy/',include('Vacancy.urls')),
    url(r'^adminprtal',include('Adminportal.urls')),

    url(r'^accounts/',include('tenantprofile.urls'))

]
