from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils.translation import gettext as _

#Vue qui gère les requêtes HTTP pour la page d'accueil de l'application main
def index(request):
    context={
        "posts": Post.objects.all()
    }
    return HttpResponse(render(request, "main/index.html", context))
