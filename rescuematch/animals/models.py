from django.db import models


class RescueCentre(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(
        upload_to="animals/",
        blank=True,
        null=True,
    )
    rescue = models.ForeignKey(
        RescueCentre,
        on_delete=models.CASCADE,
        related_name="animals",
    )
    image_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name