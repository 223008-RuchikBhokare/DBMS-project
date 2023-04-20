from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('doctors/', views.doctors, name="doctors"),
    path('patients/', views.patients,name="patients"),
    path('medrec/', views.medrec,name="medrec"),
    path('insertdoctors/', views.insertdoctors,name="insertdoctors"),
    path('insertdoctorsform/', views.insertdoctorsform,name="insertdoctorsform"),
    path('insertpatients/', views.insertpatients,name="insertpatients"),
    path('insertpatientsform/', views.insertpatientsform,name="insertpatientsform"),
    path('insertmedrec/', views.insertmedrec,name="insertmedrec"),
    path('insertmedrecform/', views.insertmedrecform,name="insertmedrecform"),
    path('delete/', views.delete,name="delete"),
    path('deleteform/', views.deleteform,name="deleteform"),
]