from django.contrib import admin
from main.models import Post
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

class PostAdmin(TranslationAdmin):
    pass

admin.site.register(Post, PostAdmin)


