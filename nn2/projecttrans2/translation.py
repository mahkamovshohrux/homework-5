from modeltranslation.translator import translator, TranslationOptions
from transapp2.models import TransModel2


class TodoTranslationOptions(TranslationOptions):
    fields = ('task_name', 'description')
    required_languages = ('uz',)


translator.register(TransModel2, TodoTranslationOptions)
