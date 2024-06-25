# main/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import Post

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')  # Les champs que vous souhaitez traduire

translator.register(Post, PostTranslationOptions)