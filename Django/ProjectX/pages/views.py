from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.





def index(response, id):
    return render(response, "")

def home(response):
    return render(response, "esileht/esileht.html")

def services(response):
    return render(response, "services/service.html")
