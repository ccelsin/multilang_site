from chatterbot import ChatBot
import spacy

spacy.cli.download("en_core_web_sm")
spacy.cli.download("en")

nlp = spacy.load('en_core_web_sm')

chatbot = ChatBot(
    'Food Advisor',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer.train(training_data)

# Training With Corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

trainer_corpus.train(
    'chatterbot.corpus.english'
)


from chatterbot.tagging import PosLemmaTagger

# Surcharge de la méthode __init__ pour utiliser le nom complet du modèle
class CustomPosLemmaTagger(PosLemmaTagger):
    def __init__(self, language=None):
        super().__init__(language)
        self.nlp = spacy.load("en_core_web_sm")

# Utiliser CustomPosLemmaTagger au lieu de PosLemmaTagger
PosLemmaTagger = CustomPosLemmaTagger