from django.urls import path, re_path

from . import views

urlpatterns = [
    path('mass_query', views.mass_query, name='mass_query'),
    path('consult_lists', views.consult_lists, name='consult_lists'),
    path('consult_lists', views.consult_lists, name='consult_lists'),
    path('report_C&C', views.report_CyC, name='report_CyC'),
    path('addList', views.addList, name='addList'),
]
