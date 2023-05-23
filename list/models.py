from django.db import models


class list_emp(models.Model):
    
    coincidences = models.BooleanField(default=True, verbose_name='Tiene coincidencias si / no')
    identification = models.CharField(max_length=100, verbose_name='Identificación')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    observations = models.TextField(null=True, blank=True, verbose_name='observaciones')
    withdrawal_date = models.DateField(null=True, verbose_name='Fecha de retiro')
    avance = models.CharField(null=True, max_length=255, verbose_name='avance')

    
    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table = 'list_emp'


class Queries_and_Coincidences(models.Model):
    
    employee = models.ForeignKey(list_emp, on_delete=models.RESTRICT)
    consul_date = models.DateTimeField(auto_now_add=True)
    record = models.BooleanField(default=False, verbose_name='Tiene coincidencias si / no')

    class Meta:
        verbose_name_plural = "Reporte Consultas & Conincidencias"
        db_table = 'Queries_and_Coincidences'