from rest_framework import serializers
from .models import list_emp


class serializersAddList(serializers.ModelSerializer):

    class Meta:
        model = list_emp
        fields = '__all__'

# -- PUT de Herramientas 
class serializerslistRecord(serializers.ModelSerializer):
    
    class Meta:
        model = list_emp
        fields = ["record"]