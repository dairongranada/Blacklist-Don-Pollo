from django.contrib import admin
from .models import list_emp
from django.contrib.auth.models import Permission

#Modelos gestionables desde la vista de administrador
admin.site.register(list_emp)

