from django import forms
from .models import ProcurementChoice, RFQbid

class ProcurementChoiceForm(forms.ModelForm):
    class Meta:
        model = ProcurementChoice
        fields = ['name']

class RFQbidForm(forms.ModelForm):
    class Meta:
        model = RFQbid
        fields = "__all__"


