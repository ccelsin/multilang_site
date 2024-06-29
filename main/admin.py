# Importation du module admin de Django
from django.contrib import admin

# Importation du modèle Post depuis l'application main
from main.models import Post

# Importation de TranslationAdmin depuis le module modeltranslation.admin
# Ce module est utilisé pour gérer la traduction des modèles dans l'interface d'administration de Django
from modeltranslation.admin import TranslationAdmin

# Définition d'une classe PostAdmin qui hérite de TranslationAdmin
# Cette classe est utilisée pour personnaliser l'affichage et le comportement du modèle Post dans l'interface d'administration
class PostAdmin(TranslationAdmin):
    pass  # Le mot clé 'pass' est utilisé pour indiquer que le corps de la classe est vide, mais qu'elle hérite toujours de TranslationAdmin

# Enregistrement du modèle Post dans l'interface d'administration de Django
# Cela permet de gérer les instances du modèle Post via l'interface d'administration
# La classe PostAdmin est passée comme second argument pour utiliser les fonctionnalités de traduction
admin.site.register(Post, PostAdmin)
