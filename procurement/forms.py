from django import forms
from .models import ProcurementChoice

class ProcurementChoiceForm(forms.ModelForm):
    class Meta:
        model = ProcurementChoice
        fields = ['name']


