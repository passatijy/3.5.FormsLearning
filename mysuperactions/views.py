from django.shortcuts import render
from django import forms

# Create your views here.

def show_basic(request):
	#form = NameForm()
	return render(request, 'forms/basic.html', {'form': 'something'})
