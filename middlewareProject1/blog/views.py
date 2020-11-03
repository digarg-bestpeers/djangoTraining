from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	print("I am View")
	return HttpResponse("This is Home Page")
