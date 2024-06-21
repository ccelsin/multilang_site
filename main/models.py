from django.db import models

from django.utils import timezone

#Création du modèle pour gérer des articles de blog avec les champs title, content, et publication_date.

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
