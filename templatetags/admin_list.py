from copy import deepcopy
from django.contrib.admin.templatetags.admin_list import register as parent_register

register = deepcopy(parent_register)

@register.inclusion_tag('admin/filter.html', takes_context=True)
def admin_list_filter(context, cl, spec):
    # Append change list params to spec object
    spec.params = cl.params
    context.update({'title': spec.title, 'choices' : list(spec.choices(cl)), 'spec': spec})
    return context
