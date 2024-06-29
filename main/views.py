from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from mychatbot.chat import get_response  # Importation de la fonction get_response du module mychatbot.chat
from .models import Post
from django.utils.translation import gettext as _

# Vue qui gère les requêtes HTTP pour la page d'accueil de l'application main
def index(request):
    # Création d'un contexte contenant tous les objets Post
    context = {
        "posts": Post.objects.all()
    }
    # Rend le template 'main/index.html' avec le contexte et retourne la réponse HTTP
    return HttpResponse(render(request, "main/index.html", context))

# Vue pour gérer les requêtes de prédiction du chatbot
def predict(request):
    # Vérification que la méthode de la requête est POST
    if request.method == "POST":
        try:
            # Chargement des données JSON depuis le corps de la requête
            data = json.loads(request.body)
            # Récupération du message depuis les données JSON
            text = data.get("message")
            # Vérification que le message n'est pas vide ou null
            if text is None or text.strip() == "":
                return JsonResponse({"error": "No message provided"}, status=400)
            # Appel de la fonction get_response pour obtenir une réponse du chatbot
            response = get_response(text)
            # Création d'un message contenant la réponse
            message = {"answer": response}
            # Retourne la réponse en format JSON
            return JsonResponse(message)
        except json.JSONDecodeError:
            # Gestion de l'erreur si les données JSON ne sont pas valides
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    # Retourne une erreur si la méthode de la requête n'est pas POST
    return JsonResponse({"error": "Invalid request method"}, status=400)
