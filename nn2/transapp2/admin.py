from django.contrib import admin
from .models import TransModel2
from .forms import TransForms2


# Register your models here.

class TransAdmim2(admin.ModelAdmin):
    form = TransForms2
    list_display = ('task_name','user','status','create')
    search_fields = ('task_name',)

admin.site.register(TransModel2,TransAdmim2)