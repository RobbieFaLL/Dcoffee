from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    # Check if the value is an instance of BoundWidget
    if hasattr(value, 'widget'):
        widget = value.widget
        # If the widget has the 'attrs' attribute, modify its class
        if 'class' in widget.attrs:
            widget.attrs['class'] += f' {arg}'
        else:
            widget.attrs['class'] = arg
        return value
    return value
