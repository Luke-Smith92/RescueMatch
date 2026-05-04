from django.shortcuts import render, get_object_or_404
from .models import Animal


def home(request):
    return render(request, "home.html")


def browse(request):
    animals = Animal.objects.all()
    return render(request, "browse.html", {"animals": animals})


def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, "animal_detail.html", {"animal": animal})