from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("browse/", views.browse, name="browse"),
    path("about/", views.about, name="about"),

    path("animal/<int:animal_id>/", views.animal_detail, name="animal_detail"),
    path("animal/<int:animal_id>/match/", views.match_animal, name="match_animal"),

    path("manage-animals/", views.manage_animals, name="manage_animals"),
    path("manage-animals/add/", views.add_animal, name="add_animal"),
    path("manage-animals/<int:animal_id>/edit/", views.edit_animal, name="edit_animal"),
    path("manage-animals/<int:animal_id>/delete/", views.delete_animal, name="delete_animal"),
]