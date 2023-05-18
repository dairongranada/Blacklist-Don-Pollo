from django.urls import path, re_path
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.db import connection

from list.utils import dictfetchall
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from django.core.files.storage import FileSystemStorage

from . import views

import os

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser])
def employee_list(request):
    """
    List all employees, or create a new employee.
    """
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT  """)

            query_res = dictfetchall(cursor)
            return JsonResponse(query_res, safe=False)
    return JsonResponse([{"error": "No autorizado"}], status=401, safe=False)