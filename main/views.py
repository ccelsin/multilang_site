from django.shortcuts import render
from django.http import JsonResponse
import json
from mychatbot.chat import get_response  # Importez votre fonction get_response
from django.http import HttpResponse
from .models import Post
from django.utils.translation import gettext as _

#Vue qui gère les requêtes HTTP pour la page d'accueil de l'application main
def index(request):
    context={
        "posts": Post.objects.all()
    }
    return HttpResponse(render(request, "main/index.html", context))

def predict(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            text = data.get("message")
            if text is None or text.strip() == "":
                return JsonResponse({"error": "No message provided"}, status=400)
            response = get_response(text)
            message = {"answer": response}
            return JsonResponse(message)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=400)
