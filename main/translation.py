from modeltranslation.translator import translator, TranslationOptions
from .models import Post

# for Post model
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',' publication_date','post_image')

translator.register(Post, PostTranslationOptions)