from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import logout
from django.views.generic import RedirectView
from MainSystem import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

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
    url(r'^adminprtal/',include('Adminportal.urls')),


    url('^register/', CreateView.as_view(
        template_name='registration/registeruser.html',
        form_class=UserCreationForm,
        success_url='homepage/'
    )),



]

# Change admin look

admin.site.site_header = ("My House Management System")
admin.site.site_title= "My House System Admin"