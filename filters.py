#coding: utf-8
from django import forms
from django.contrib.admin.filters import ListFilter
from django.contrib.admin.views.main import IGNORED_PARAMS


class BaseInputFilter(ListFilter):
    is_search_filter = True
    form_template = 'inputfilters/form.html'
    
    def __init__(self, request, params, model, model_admin):
        super(BaseInputFilter, self).__init__(request, params, model, model_admin)
        
        fields = {}
        for k, v in request.GET.items():
            if k not in IGNORED_PARAMS and k not in self.form.base_fields:
                fields.setdefault(k, forms.CharField(widget=forms.HiddenInput)).initial = v
        
        self.form = type('InputFilterForm', (self.form,), fields)(request.GET)
        for field in self.form.fields.values():
            field.required = False
        
        for p in self.expected_parameters():
            if p in params:
                value = params.pop(p)
                self.used_parameters[p] = value
    
    def expected_parameters(self):
        for field in self.form.fields:
            yield field
    
    def has_output(self):
        return True
    
    def choices(self, cl):
        return ()