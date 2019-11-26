from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'Do_dogs_have_money_Website/index.html')
