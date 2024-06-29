from django.shortcuts import render
from django.http import JsonResponse
import json
from .chat import get_response  # Importez votre fonction get_response

def index(request):
    return render(request, 'mychatbot/base.html')

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
