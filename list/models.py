from django.db import models


class list_emp(models.Model):
    
    identification = models.CharField(max_length=30, verbose_name='Identificación')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    observations = models.CharField(max_length=255)
    withdrawal_date = models.DateField(verbose_name='Fecha de retiro')
    avance = models.CharField(max_length=255, verbose_name='avance')
    history = models.BooleanField(default=False, verbose_name='Revisado si o no')

    
    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table = 'list_emp'

