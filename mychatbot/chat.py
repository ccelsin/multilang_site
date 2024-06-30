"""import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Détection du dispositif à utiliser pour les calculs : GPU (cuda) si disponible, sinon CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Ouverture et chargement du fichier intents.json contenant les intentions et les réponses du chatbot
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

# Chemin vers le fichier contenant les paramètres entraînés du modèle
FILE = "data.pth"
# Chargement des données du modèle depuis le fichier
data = torch.load(FILE)

# Extraction des paramètres du modèle depuis les données chargées
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Initialisation du modèle de réseau de neurones avec les paramètres extraits
model = NeuralNet(input_size, hidden_size, output_size).to(device)
# Chargement des poids du modèle à partir de l'état sauvegardé
model.load_state_dict(model_state)
# Mise du modèle en mode évaluation (inférence)
model.eval()

bot_name = "Celsin"

def get_response(msg):
    # Tokenisation du message utilisateur
    sentence = tokenize(msg)
    # Conversion du message tokenisé en sac de mots (bag of words)
    X = bag_of_words(sentence, all_words)
    # Reshape du vecteur d'entrée pour correspondre aux attentes du modèle
    X = X.reshape(1, X.shape[0])
    # Conversion du vecteur en tenseur PyTorch et transfert vers le dispositif approprié
    X = torch.from_numpy(X).to(device)

    # Passage du tenseur à travers le modèle pour obtenir les prédictions
    output = model(X)
    # Récupération de l'indice de la classe prédite avec la plus haute probabilité
    _, predicted = torch.max(output, dim=1)

    # Récupération de l'étiquette correspondante à la classe prédite
    tag = tags[predicted.item()]

    # Calcul des probabilités pour chaque classe
    probs = torch.softmax(output, dim=1)
    # Récupération de la probabilité de la classe prédite
    prob = probs[0][predicted.item()]
    # Si la probabilité est supérieure à un seuil (0.75), on considère la prédiction comme valide
    if prob.item() > 0.75:
        for intent in intents['intents']:
            # Si l'étiquette correspond à l'une des intentions, on retourne une réponse aléatoire parmi celles définies pour cette intention
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    # Si aucune intention n'a été reconnue avec une probabilité suffisante, on retourne un message par défaut
    return "Je ne comprends pas ..."

# Bloc principal pour les tests interactifs
if __name__ == "__main__":
    
    while True:
        # Lecture de l'entrée utilisateur
        sentence = input("You: ")
        # Si l'utilisateur tape "quit", on sort de la boucle
        if sentence == "quit":
            break

        # Obtention de la réponse du chatbot pour le message utilisateur
        resp = get_response(sentence)
        # Affichage de la réponse
        print(resp)
"""