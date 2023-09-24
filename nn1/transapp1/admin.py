from django.contrib import admin
from .models import TransModel1
from .forms import TransForms1


# Register your models here.

class TransAdmim1(admin.ModelAdmin):
    form = TransForms1
    list_display = ('task_name','user','status','create')
    search_fields = ('task_name',)

admin.site.register(TransModel1,TransAdmim1)