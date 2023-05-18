from django import template
import datetime
from django.contrib.humanize.templatetags.humanize import intcomma
from decimal import Decimal
register = template.Library()

@register.filter(name='format_currency')
def format_currency(value):
   
    tmp_value=Decimal(value)
    return "$%s" % (intcomma(int(tmp_value)))

@register.filter(name='get_first_char')
def get_first_char(value):
  return value[0].upper()

@register.filter(name='trim')
def trim(value):
    return value.strip()

@register.filter(name='to_date')
def to_date(value,format):

  tmp_date=value.strip()
  date_time_obj = datetime.datetime.strptime(tmp_date, f'{format}')

  return date_time_obj.strftime("%d/%m/%Y")


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

