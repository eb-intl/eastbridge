from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Section


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
