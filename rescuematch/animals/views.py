from django.shortcuts import render
from .models import Animal


def home(request):
    return render(request, "home.html")


def browse(request):
    animals = Animal.objects.all()
    return render(request, "browse.html", {"animals": animals})