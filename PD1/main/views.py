from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request, 'index.html')

def programingLanguages(request):
    return render(request, 'main/index.html')