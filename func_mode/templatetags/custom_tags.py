from django import template
register = template.Library()

@register.filter(name='change_float')
def change_float(valor:int) -> str:
    return str(valor).replace(',','.')

@register.filter(name='checkbox')
def checkbox(valor:bool) -> str:
    return 'checked' if valor is True else ''
