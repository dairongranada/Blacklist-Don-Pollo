from django.db import models
from django.contrib.auth import get_user_model

from django.utils.html import mark_safe
User = get_user_model()


# class Name_table(models.Model):
#     # name = models.CharField(max_length=100, verbose_name='Nombre')

#     def __str__(self) -> str:
#         return f'{self.name}'

#     class Meta:
#         verbose_name = "description"
#         verbose_name_plural = "description"
#         db_table = 'name table'


