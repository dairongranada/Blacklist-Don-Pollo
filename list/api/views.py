import pandas as pd
import csv
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.db import connection

from list.utils import dictfetchall
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from django.core.files.storage import FileSystemStorage


from list.models  import list_emp
from list.serializers import serializersAddList

from datetime import datetime

@api_view(['GET'])
@parser_classes([MultiPartParser])
def employee_list(request):
    """
    List all employees, or create a new employee.
    """
    if request.method == 'GET':
        records = list_emp.objects.all()
        serializer = serializersAddList(records, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse([{"error": "No autorizado"}], status=401, safe=False)


@api_view(['POST'])
@parser_classes([MultiPartParser])
def employees_imported(request):
    """ Import employees for convert in SIESA FILE """

    existing_records = 0

                                   
    if request.method == 'POST':
        
        uploaded_file = request.FILES['COLABORADORES']
      
        dataframe = pd.read_excel(uploaded_file)

        for _, row in dataframe.iterrows():
            print(row)
            iden = row['CEDULA']
            name = row['NOMBRE EMPLEADO EX-EMPLEADO']
            with_date = row['FECHA DE RETIRO']
            observ = row['OBSERVACIONES']
            avan = row['AVANCE']
            # ceo = row['VALIDACIÓN CEO']



            existing_records = list_emp.objects.filter(
                identification = iden, name = name, observations = observ, avance = avan).count()
            
            if existing_records == 0:
                
                list_emp.objects.create(
                    identification = iden, 
                    name = name,
                    withdrawal_date = with_date,
                    observations = observ,
                    avance = avan
                )
                
        if existing_records >= 1:
            return JsonResponse({"warning":True,'msg':'Aparecer habían ex empleados repetidos y solo se guardaron los que no estaban en la base de datos'}, status=200, safe=False)
        return JsonResponse({"warning":False, 'msg':'Ex Empleados Guardados Correctamente'}, status=200, safe=False)

    return JsonResponse([{"error": "No autorizado"}], status=401, safe=False)



@api_view(['GET'])
def individual_consultation(request,pk):

    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM list_emp WHERE identification = {pk};")
            query_res = dictfetchall(cursor)

            return JsonResponse(query_res, safe=False)

    return JsonResponse([{"error": "No autorizado"}], status=401, safe=False)



@api_view(['GET'])
def queries_coincidences(request, fecha_inicio, fecha_fin):

    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute(f"""  
                SELECT * FROM list_emp
                WHERE withdrawal_date >= '{fecha_inicio}' AND withdrawal_date <= '{fecha_fin}';
            """)
            query_res = dictfetchall(cursor)

            return JsonResponse(query_res, safe=False)

    return JsonResponse([{"error": "No autorizado"}], status=401, safe=False)












