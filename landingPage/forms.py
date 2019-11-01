from django import forms
from .models import StatusModels

class StatusForms(forms.ModelForm):
	status = forms.CharField()
	
	class Meta:
		model = StatusModels
		fields = '__all__'