from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('animal/<int:animal_id>/', views.animal_detail, name='animal_detail'),
]