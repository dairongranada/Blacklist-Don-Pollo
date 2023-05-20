from django.db import models


class list_emp(models.Model):
    
    identification = models.CharField(max_length=100, verbose_name='Identificación')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    observations = models.TextField(null=True,blank=True, verbose_name='observaciones')
    withdrawal_date = models.DateField(verbose_name='Fecha de retiro')
    avance = models.CharField(max_length=255, verbose_name='avance')
    record = models.BooleanField(default=False, verbose_name='Revisado si o no')

    
    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table = 'list_emp'

class Queries_and_Coincidences(models.Model):
    employee = models.ForeignKey(list_emp, on_delete=models.RESTRICT)
    consultation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reporte Consultas & Conincidencias"
        db_table = 'Queries_and_Coincidences'