# Importation du module translator et de la classe TranslationOptions depuis modeltranslation.translator
# Ces importations sont nécessaires pour configurer les options de traduction pour un modèle Django
from modeltranslation.translator import translator, TranslationOptions

# Importation du modèle Post depuis le module models de l'application actuelle
# Cela permet d'appliquer les options de traduction à ce modèle
from .models import Post

# Définition d'une classe PostTranslationOptions qui hérite de TranslationOptions
# Cette classe est utilisée pour spécifier les champs du modèle Post qui doivent être traduits
class PostTranslationOptions(TranslationOptions):
    # Définition des champs du modèle Post qui seront traduits
    fields = ('title', 'content')  # Les champs que vous souhaitez traduire

# Enregistrement du modèle Post avec les options de traduction spécifiées dans PostTranslationOptions
# Cela configure les traductions pour le modèle Post en utilisant les champs spécifiés
translator.register(Post, PostTranslationOptions)
