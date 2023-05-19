from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.db import connection

from list.utils import dictfetchall
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from django.core.files.storage import FileSystemStorage


from list.models  import list_emp
from list.serializers import serializersAddList


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
def employees_concepts_imported(request):
    """ Import employees for convert in SIESA FILE """
                                   

    #Solo el elaborador puede cargar archivos
    if request.method == 'POST':
        
        uploaded_file = request.FILES['concepts']

        # tamaño del archivo en MB
        file_size = round(uploaded_file.size/1048576, 2)

        if (uploaded_file.content_type != 'text/csv'):

            return JsonResponse([{"error": "Solo se admiten archivos en formato csv"}], status=400, safe=False)
        if (file_size > 5):

            return JsonResponse([{"error": "El tamaño del archivo supera los 5 MB"}], status=400, safe=False)

        fs = FileSystemStorage()

        
        return JsonResponse(data, safe=False)
    return JsonResponse([{"error": "No autorizado"}], status=401, safe=False)