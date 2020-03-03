from django import template

register = template.Library()

@register.simple_tag
def price_sale(price, sale):
    return round(price * (1-(sale/100)), 2)
