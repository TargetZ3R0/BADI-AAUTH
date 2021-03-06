from django import forms
from django.utils.translation import ugettext_lazy as _


class OpForm(forms.Form):
    doctrine = forms.CharField(max_length=254, required=True, label=_('Doctrine'))
    system = forms.CharField(max_length=254, required=True, label=_("System"))
    start = forms.DateTimeField(required=True, label=_("Start Time"))
    duration = forms.CharField(max_length=254, required=True, label=_("Duration"))
    operation_name = forms.CharField(max_length=254, required=True, label=_("Operation Name"))
    fc = forms.CharField(max_length=254, required=True, label=_("Fleet Commander"))
    operation_modifier = forms.CharField(max_length=2, required=False, label=_("Space Point Modifier")) #RAR 20180312 Added; Future proof for space point modifier for op. 
