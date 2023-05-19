from django.urls import path, re_path
from . import views

urlpatterns = [
    path('employees', views.employee_list),
    path('cargar-excel/', views.employees_imported),

]