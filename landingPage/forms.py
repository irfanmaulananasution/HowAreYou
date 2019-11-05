from django import forms
from .models import StatusModels

class StatusForms(forms.ModelForm):
	status = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "form-control",
		"placeholder" : "Gimana kabarmu hari ini?",
		"required" : True
	}))
	
	class Meta:
		model = StatusModels
		fields = '__all__'
		