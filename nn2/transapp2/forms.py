from django import forms
from .models import TransModel2

class TransForms2(forms.ModelForm):
    task_name_uz = forms.CharField()
    task_name_ru = forms.CharField()
    task_name_en = forms.CharField()

    deskription_uz = forms.CharField()
    deskription_ru = forms.CharField()
    deskription_en = forms.CharField()
    class Meta:
        model = TransModel2
        exclude = ('task_name', 'description')
