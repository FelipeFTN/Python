from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, World!")

def felipe(request):
    return HttpResponse("Hello, Felipe!")