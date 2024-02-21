from django import forms
from .models import *

class user_signup(forms.ModelForm):
    class Meta:
        model=hexauser
        fields='__all__'