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

@register.simple_tag
def totalbox(plus,good,minus,special):
    try:
        result = plus + good + minus + special*2
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return 'Fail'
    
@register.simple_tag
def complaintbox(plus,minus,special):
    try:
        result = plus + minus + special*2
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return 'Fail'
    
@register.simple_tag
def missingbox(cbox,stockbox):
    try:
        result = stockbox - cbox 
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return 'None'

@register.simple_tag
def propercentage(pouchcount,planbox):
    try:
        result = (pouchcount*10) / planbox 
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return 'Fail'