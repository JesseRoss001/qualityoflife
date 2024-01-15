from django import template
from django.db.models.fields import Field

register = template.Library()

@register.filter
def get_fields(obj):
    return [field for field in obj._meta.get_fields() if isinstance(field, Field)]

@register.filter
def get_field_value(field, obj):
    return field.value_from_object(obj)

@register.filter(name='index')
def get_by_index(value, arg):
    return value[int(arg)]