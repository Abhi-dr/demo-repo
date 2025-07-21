from django.shortcuts import render, redirect

from .models import DareExchange

from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, "home/home.html")

# =================================== DARES =============================

def dares(request):

    dares = DareExchange.objects.all()

    parameters = {
        "dares": dares
    }

    return render(request, "home/dares.html", parameters)

