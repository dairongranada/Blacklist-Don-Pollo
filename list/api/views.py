import pandas as pd
import csv
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse,HttpResponseNotFound
from django.db import connection

from list.utils import dictfetchall
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes


from list.models  import list_emp, Queries_and_Coincidences
from list.serializers import serializersAddList,CoincidencesSerializers

from datetime import datetime

from django.http import FileResponse
from django.views import View
import os

@api_view(['GET'])
@parser_classes([MultiPartParser])
def employee_list(request):
    """
    List all employees
    """
    if request.method == 'GET':
        records = list_emp.objects.all()
        serializer = serializersAddList(records, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse([{"error": "No autorizado"}], status=401, safe=False)


@api_view(['POST'])
@parser_classes([MultiPartParser])
def employees_imported(request):
    """
    create a new employee.
    """

    existing_records = 0

    if request.method == 'POST':
        
        uploaded_file = request.FILES['LISTA_INTERNA']
      
        dataframe = pd.read_excel(uploaded_file)

        for _, row in dataframe.iterrows():
            iden = row['CEDULA']
            name = row['NOMBRE EMPLEADO EX-EMPLEADO']
            with_date = row['FECHA DE RETIRO']
            observ = row['OBSERVACIONES']
            avan = row['AVANCE']
            # ceo = row['VALIDACIÓN CEO']


            existing_records = list_emp.objects.filter(identification = iden, name = name).count()
            
            if existing_records == 0:
                list_emp.objects.create(
                    identification = iden, name = name, withdrawal_date = with_date, observations = observ, avance = avan
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
                SELECT * FROM list_emp emp INNER JOIN queries_and_coincidences qc ON emp.id = qc.employee_id 
                WHERE qc.consul_date >= '{fecha_inicio}' AND qc.consul_date <= '{fecha_fin}';
            """)
            query_res = dictfetchall(cursor)

            return JsonResponse(query_res, safe=False)

    return JsonResponse([{"error": "No autorizado"}], status=401, safe=False)




@api_view(['POST'])
@parser_classes([MultiPartParser])
def employee_mass_query(request):

    existing_employees = []
    non_existent_employees = []

    if request.method == 'POST':
        
        uploaded_file = request.FILES['LISTA_INTERNA']
        dataframe = pd.read_excel(uploaded_file)

        for _, row in dataframe.iterrows():
            iden = row['CEDULA']
            name = row['NOMBRE EMPLEADO EX-EMPLEADO']

            # Descomentar si es el caso que en la consulta masiva se ingrese esos datos..
            # with_date = row['FECHA DE RETIRO']
            # observ = row['OBSERVACIONES']
            # avan = row['AVANCE']

            try:
                employee = list_emp.objects.get(identification=iden, coincidences=1)

                existing_employees.append({
                    "identification" : iden,
                    "name" : employee.name,
                    "with_date": employee.withdrawal_date,
                    "observation" : employee.observations,
                    "avance" : employee.avance,
                })

                data = { "employee": employee.id, "consul_date":datetime.now(), "record": True }

                serializer = CoincidencesSerializers(data = data)
                if serializer.is_valid():
                    serializer.save()

            except list_emp.DoesNotExist:
                employeeNot = list_emp.objects.get(identification=iden, coincidences=0)

                print()
                print()
                print()
                print(employeeNot)
                print()
                if employeeNot:
                    none_funtion = True
                else:
                    list_emp.objects.create(
                        identification = iden, 
                        name = name, 
                        withdrawal_date = None, 
                        observations = None, 
                        avance = None,
                        coincidences = False
                    )

                non_existent_employees.append({
                    "identification" : iden,
                    "name" : name,
                    # "with_date": with_date,
                    # "observation" : observ,
                    # "avance" : avan,
                })

                
        return JsonResponse({"warning":False, 'non_existent_employees':non_existent_employees,  'existing_employees':existing_employees,  'msg':'Datos generados correctamente'}, status=200, safe=False)

    return JsonResponse([{"error": "No autorizado"}], status=401, safe=False)




class DescargarArchivoAPI(View):
    def get(self, request, archivo_nombre):
        # Obtener la ruta completa al archivo
        archivo_ruta = os.path.join('media', archivo_nombre)
        
        # Verificar si el archivo existe
        if os.path.exists(archivo_ruta):
            # Abrir el archivo en modo binario
            with open(archivo_ruta, 'rb') as archivo:
                # Crear una respuesta de archivo y especificar el tipo de contenido
                response = FileResponse(archivo)
                response['Content-Disposition'] = f'attachment; filename="{archivo_nombre}"'
                return response
        else:
            # Manejar caso de archivo no encontrado
            return HttpResponseNotFound('Archivo no encontrado')



