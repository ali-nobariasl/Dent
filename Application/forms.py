from django import forms

from .models import first

class firstform(forms.Form):
    class Meta:
        model= first
        fields = '__all__'