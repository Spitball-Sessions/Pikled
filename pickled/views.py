from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is the Pick'led app.  Welcome to fermentation town!")
