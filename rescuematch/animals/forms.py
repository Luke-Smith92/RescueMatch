from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            "name",
            "animal_type",
            "breed",
            "age",
            "description",
            "image",
            "rescue",
            "image_name",
        ]