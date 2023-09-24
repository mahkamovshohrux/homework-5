from django import forms
from .models import TransModel3

class TransForms3(forms.ModelForm):
    task_name_uz = forms.CharField()
    task_name_ru = forms.CharField()
    task_name_en = forms.CharField()

    deskription_uz = forms.CharField()
    deskription_ru = forms.CharField()
    deskription_en = forms.CharField()
    class Meta:
        model = TransModel3
        exclude = ('task_name', 'description')
