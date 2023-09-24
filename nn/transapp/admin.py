from django.contrib import admin
from .models import TransModel
from .forms import TransForms


# Register your models here.

class TransAdmim(admin.ModelAdmin):
    form = TransForms
    list_display = ('task_name','user','status','create')
    search_fields = ('task_name',)

admin.site.register(TransModel,TransAdmim)