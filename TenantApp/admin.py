from django.contrib import admin
from TenantApp.models import MovingInInstructions,MovingOutInstructions
# Register your models here.
admin.site.register(MovingInInstructions)
admin.site.register(MovingOutInstructions)