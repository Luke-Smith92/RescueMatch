from django.shortcuts import render, get_object_or_404
from .models import Animal


def home(request):
    return render(request, "home.html")


def browse(request):
    animals = Animal.objects.all()
    return render(request, "browse.html", {"animals": animals})


def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    previous_animal = Animal.objects.filter(id__lt=animal.id).order_by('-id').first()
    next_animal = Animal.objects.filter(id__gt=animal.id).order_by('id').first()

    return render(request, "animal_detail.html", {
        "animal": animal,
        "previous_animal": previous_animal,
        "next_animal": next_animal,
        "matched": False,
    })


def match_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    previous_animal = Animal.objects.filter(id__lt=animal.id).order_by('-id').first()
    next_animal = Animal.objects.filter(id__gt=animal.id).order_by('id').first()

    return render(request, "animal_detail.html", {
        "animal": animal,
        "previous_animal": previous_animal,
        "next_animal": next_animal,
        "matched": True,
    })
def about(request):
    return render(request, "about.html")