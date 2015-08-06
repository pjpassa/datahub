from django import template


register = template.Library()


@register.filter('widget_type')
def widget_type(field):
    return field.field.widget.__class__.__name__