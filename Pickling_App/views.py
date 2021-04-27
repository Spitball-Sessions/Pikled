from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(
        "There is nothing here yet.  You probably wanted the <a href='http://127.0.0.1:8000/pickled'>Pickled</a> page")

