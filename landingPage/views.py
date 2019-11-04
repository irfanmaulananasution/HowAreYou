from django.shortcuts import render, redirect
from .forms import StatusForms
from .models import StatusModels

def landingPage(request):
	form = StatusForms()
	model = StatusModels.objects.all() if StatusModels.objects.all() else None
	
	if request.method == "POST":
		form = StatusForms(request.POST)
		if form.is_valid():
			form.save()
			return redirect('landingPage:landingPage')
			
			
	response = {
		'form' : form,
		'schedule' : model,
		}
	return render(request, 'landingPage.html', response)
