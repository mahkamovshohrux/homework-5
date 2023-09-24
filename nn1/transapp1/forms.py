from django import forms
from .models import TransModel1

class TransForms1(forms.ModelForm):
    task_name_uz1 = forms.CharField()
    task_name_ru1 = forms.CharField()
    task_name_en1 = forms.CharField()

    deskription_uz1 = forms.CharField()
    deskription_ru1 = forms.CharField()
    deskription_en1 = forms.CharField()
    class Meta:
        model = TransModel1
        exclude = ('task_name', 'description')
