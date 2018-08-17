from django import template
register = template.Library()

@register.simple_tag
def url_add(request):
    print("A")