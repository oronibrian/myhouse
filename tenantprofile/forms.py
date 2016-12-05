from django import forms
from models import  TenantProfile

class UserProfileForm(forms.ModelForm):
    model = TenantProfile
    fields=('full name','email')