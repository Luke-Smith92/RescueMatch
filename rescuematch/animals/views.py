from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal
from .forms import AnimalForm


def home(request):
    return render(request, "home.html")

def rescue_login(request):
    if request.method == "POST":
        return redirect("manage_animals")

    return render(request, "rescue_login.html")

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


def manage_animals(request):
    animals = Animal.objects.all()
    return render(request, "manage_animals.html", {"animals": animals})


def add_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("manage_animals")
    else:
        form = AnimalForm()

    return render(request, "animal_form.html", {
        "form": form,
        "page_title": "Add Animal",
        "button_text": "Add Animal",
    })


def edit_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect("manage_animals")
    else:
        form = AnimalForm(instance=animal)

    return render(request, "animal_form.html", {
        "form": form,
        "page_title": "Edit Animal",
        "button_text": "Save Changes",
    })


def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        animal.delete()
        return redirect("manage_animals")

    return render(request, "delete_animal.html", {"animal": animal})


def about(request):
    return render(request, "about.html")