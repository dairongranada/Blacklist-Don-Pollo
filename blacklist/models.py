from django.db import models
from django.contrib.auth import get_user_model

from django.utils.html import mark_safe
User = get_user_model()




class List_Employee(models.Model):

    identification = models.CharField(max_length=30, verbose_name='Identificación')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    observations = models.CharField(max_length=255)
    withdrawal_date = models.DateField(verbose_name='Fecha de retiro')
    avance = models.DateField(verbose_name='avance')
    is_history = models.BooleanField(default=False, verbose_name='Revisado si o no')

    
    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = "list_employees"
        verbose_name_plural = "list_employees"
        db_table = 'list_employees'

