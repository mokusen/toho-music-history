from django import template
register = template.Library()

@register.simple_tag
def url_add(request, num):
    return_dict = request.GET.copy()
    return_dict['page'] = num
    return return_dict.urlencode()

@register.simple_tag
def sort_add(request, param):
    return_dict = request.GET.copy()
    return_dict['sort'] = str(param)
    return return_dict.urlencode()
