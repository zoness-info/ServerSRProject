from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    try:
        return value - arg
    except (TypeError, ValueError):
        return 'Fail'
    
@register.filter   
def add(value, arg):
    try :
        return value + arg
    except(TypeError, ValueError):
        return 'Fail'
    
@register.filter   
def percentage(value, arg):
    try:
        result = (value / arg) * 100
        return f'{result:.2f}'
    except (ZeroDivisionError, TypeError, ValueError):
        return 'Fail'