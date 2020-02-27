from django.http import HttpResponse
from django.shortcuts import render 

# Create your views here.
def home(request):
    context = {"text": "Hello World!!", "title": "Home"}
    return render(request, "home.html", context)

def index(request):
    context={}
    return render(request, "index.html", context)