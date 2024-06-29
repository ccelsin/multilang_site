from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from main.models import Post
import json
from mychatbot.chat import get_response

# Vue pour gérer la recherche de posts
def search_posts(request):
    query = request.GET.get('q')  # Récupère la requête de recherche depuis les paramètres GET
    results = []
    
    if query:
        # Recherche des posts contenant le mot-clé dans le titre ou le contenu
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    # Rend le template 'search/result.html' avec les résultats de la recherche
    return render(request, 'search/result.html', {'query': query, 'results': results})

# Vue pour afficher les détails d'un post spécifique
def post_detail(request, id):
    # Récupère le post correspondant à l'id, ou renvoie une 404 si non trouvé
    post = get_object_or_404(Post, id=id)
    # Rend le template 'post_detail.html' avec le post récupéré
    return render(request, 'post_detail.html', {'post': post})

# Vue pour gérer les requêtes de prédiction du chatbot
def predict(request):
    if request.method == "POST":
        try:
            # Charge les données JSON depuis le corps de la requête
            data = json.loads(request.body)
            # Récupère le message utilisateur depuis les données JSON
            text = data.get("message")
            # Vérifie que le message n'est pas vide ou null
            if text is None or text.strip() == "":
                return JsonResponse({"error": "No message provided"}, status=400)
            # Appelle la fonction get_response pour obtenir une réponse du chatbot
            response = get_response(text)
            # Crée une réponse JSON avec la réponse du chatbot
            message = {"answer": response}
            return JsonResponse(message)
        except json.JSONDecodeError:
            # Gère les erreurs si les données JSON ne sont pas valides
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    # Retourne une erreur si la méthode de la requête n'est pas POST
    return JsonResponse({"error": "Invalid request method"}, status=400)
