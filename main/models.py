from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

#Création du modèle pour gérer des articles de blog avec les champs title, content, et publication_date et post_image.

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self) -> str:
        return self.title
