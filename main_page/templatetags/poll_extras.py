from django import template

register = template.Library()


@register.filter
def subtraction(val1, val2):
    return int(val1 - val2 + 1)


@register.filter
def one_more(_1, _2):
    return _1, _2


@register.filter
def special_subtraction(_val1_val2, _val3):
    _val1, _val2 = _val1_val2
    return _val1 - _val2 * _val3

