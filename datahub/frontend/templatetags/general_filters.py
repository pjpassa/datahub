from django import template


register = template.Library()

@register.filter('type_widget')
def type_widget(field):
    return field.field.widget.__class__.__name__


@register.filter('form_type')
def form_type(form):
    for field in form:
        print(type_widget(field) == "ClearableFileInput")
        if "ClearableFileInput" == str(type_widget(field)):
            return 'enctype=multipart/form-data'
    return ""
