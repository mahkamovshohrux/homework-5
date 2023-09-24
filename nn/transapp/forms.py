from django import forms
from .models import TransModel

class TransForms(forms.ModelForm):
    task_name_uz = forms.CharField()
    task_name_ru = forms.CharField()
    task_name_en = forms.CharField()

    deskription_uz = forms.CharField()
    deskription_ru = forms.CharField()
    deskription_en = forms.CharField()
    class Meta:
        model = TransModel
        exclude = ('task_name', 'description')
