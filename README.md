# Multilang Site with Chatbot

Ce projet est une application Django multilingue intégrant un chatbot basé sur un modèle de réseau de neurones.

## Prérequis

Assurez-vous d'avoir les logiciels suivants installés sur votre machine :

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (optionnel mais recommandé)

## Installation

### Cloner le dépôt

Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/ccelsin/multilang_site.git
cd multilang_site

Créez un environnement virtuel pour isoler les dépendances du projet :

python -m venv venv

Activer la machine virtuelle:

venv\Scripts\activate

Installer les dépendances

pip install -r requirements.txt

Configuration de la base de données
Appliquez les migrations pour configurer la base de données :
python manage.py makemigrations
python manage.py migrate


Pour lancer le serveur de développement Django, utilisez la commande suivante :
python manage.py runserver

Internationalisation
Ce projet supporte l'internationalisation. Pour créer des fichiers de traduction, utilisez les commandes suivantes :

