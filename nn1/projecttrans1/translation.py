from modeltranslation.translator import translator, TranslationOptions
from transapp1.models import TransModel1


class TodoTranslationOptions(TranslationOptions):
    fields = ('task_name', 'description')
    required_languages = ('uz',)


translator.register(TransModel1, TodoTranslationOptions)
