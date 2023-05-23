from rest_framework import serializers
from .models import list_emp, Queries_and_Coincidences


class serializersAddList(serializers.ModelSerializer):

    class Meta:
        model = list_emp
        fields = '__all__'




class CoincidencesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Queries_and_Coincidences
        fields = ['employee','consul_date','record']  