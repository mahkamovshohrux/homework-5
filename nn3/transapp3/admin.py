from django.contrib import admin
from .models import TransModel3
from .forms import TransForms3


# Register your models here.

class TransAdmim3(admin.ModelAdmin):
    form = TransForms3
    list_display = ('task_name','user','status','create')
    search_fields = ('task_name',)

admin.site.register(TransModel3,TransAdmim3)