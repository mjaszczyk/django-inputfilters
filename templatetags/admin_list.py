from copy import deepcopy
from django.contrib.admin.templatetags.admin_list import register as parent_register

register = deepcopy(parent_register)

@register.inclusion_tag('admin/filter.html')
def admin_list_filter(cl, spec):
    # Append change list params to spec object
    spec.params = cl.params
    return {'title': spec.title, 'choices' : list(spec.choices(cl)), 'spec': spec}