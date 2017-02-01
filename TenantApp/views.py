from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
import datetime
from MainSystem.models import Tenant
from  TenantApp.models import MovingInInstructions,MovingOutInstructions
from  django.contrib.auth.models import User

# Create your views here.


@login_required
def tenant(request):
    template = loader.get_template('TenantApp/tenant.html')

    result = []
    movinininstruction = MovingInInstructions.objects.get()
    movingoutinstruction = MovingOutInstructions.objects.get()

    username = request.user.username
    firstname = request.user.first_name
    print(username)
    tenants = (
        Tenant.objects.all().filter(username=username)

            .prefetch_related('reminder_set'))
    for t in tenants:
        rounded_trend = [round(v, 2) for v in t.trend()]
        current_trend = rounded_trend[-1]
        float_rent = float(t.rent())
        if current_trend < -1.2 * float_rent:
            css = "danger"
        elif current_trend < -0.2 * float_rent:
            css = "warning"
        else:
            css = ""
        if t.has_left():
            css += " gone"

        expired = t.expired_reminders_count()
        if expired > 0:
            reminder_css = "btn-danger"
            reminders_count = expired
        else:
            reminder_css = ""
            reminders_count = t.pending_reminders_count()
        result.append({
            "tenant": t,
            "css": css,
            "normal_min": json.dumps(float_rent),
            "trend": json.dumps(rounded_trend),
            "reminder_css": reminder_css,
            "reminders_count": reminders_count
        })
    context = {'tenants': result,
               'movinininstruction': movinininstruction,
               'movingoutinstruction':movingoutinstruction

               }
    return HttpResponse(template.render(context, request))

@login_required
def tenant_cashflows(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    context = {'cashflows': tenant.cashflows()}
    return render(request, 'TenantApp/cashflows.html', context)

