from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponseRedirect
from  forms import UserProfileForm
from django.core.context_processors import csrf
from django .contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    if request.method =='post':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login/')
        else:
            user = request.user
            profile= user.tenantprofile
            form = UserProfileForm(instance=profile)

        args={}
        args['']=form
        return render_to_response('tenantprofile/profile.html',args)




