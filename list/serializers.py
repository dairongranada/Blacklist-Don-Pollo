from rest_framework import serializers
from .models import list_emp


class serializersAddList(serializers.ModelSerializer):

    class Meta:
        model = list_emp
        fields = '__all__'

