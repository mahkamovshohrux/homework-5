from modeltranslation.translator import translator, TranslationOptions
from transapp3.models import TransModel3


class TodoTranslationOptions(TranslationOptions):
    fields = ('task_name', 'description')
    required_languages = ('uz',)


translator.register(TransModel3, TodoTranslationOptions)
