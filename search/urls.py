from django.urls import path, include
from . import views

# Définition des urlpatterns pour l'application
urlpatterns = [
    # URL pour la vue de recherche de posts
    path('search/', views.search_posts, name='search_posts'),
    # URL pour afficher les détails d'un post spécifique
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    # Inclusion des URL de l'application 'main'
    path('', include('main.urls')),
]
