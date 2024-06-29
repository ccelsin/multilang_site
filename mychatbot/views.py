from django.shortcuts import render
from django.http import JsonResponse
import json
from .chat import get_response  # Importez votre fonction get_response

def index(request):
    return render(request, 'mychatbot/base.html')

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
