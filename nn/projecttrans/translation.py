from modeltranslation.translator import translator, TranslationOptions
from transapp.models import TransModel


class TodoTranslationOptions(TranslationOptions):
    fields = ('task_name', 'description')
    required_languages = ('uz',)


translator.register(TransModel, TodoTranslationOptions)
