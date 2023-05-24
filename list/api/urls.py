from django.urls import path, re_path
from . import views

urlpatterns = [
    path('employees', views.employee_list),
    path('cargar-excel/', views.employees_imported),
    path('individual_consultation/<int:pk>', views.individual_consultation),
    path('queries_coincidences/<str:fecha_inicio>/<str:fecha_fin>', views.queries_coincidences),
    path('mass_query', views.employee_mass_query),

    # path('descargar-archivo/<str:archivo_nombre>/', views.DescargarArchivoAPI.as_view(), name='descargar_archivo_api'),

]