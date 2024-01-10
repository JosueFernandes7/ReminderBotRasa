from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from db import MongoDBConnection
from config import settings

class ActionTarefa(Action):
    def name(self):
        return 'action_salvar_tarefa'

    def run(self, dispatcher, tracker, domain):

        nome_usuario = tracker.get_slot('nome_usuario')
        nome_tarefa = tracker.get_slot('nome_tarefa')

        if nome_tarefa and nome_usuario:
            dispatcher.utter_message(f"Tarefa: {nome_tarefa}\nUsuário: {nome_usuario}\nTarefa Cadastrada com Sucesso")
            # Example of using the class
            connection = MongoDBConnection(settings.DB_NAME)
            connection.connect()

            # Perform database operations here, for example:
            collection = connection.db[settings.DB_COLLECTION]
            document = {
                "nome_usuario": nome_usuario,
                "nome_tarefa": nome_tarefa
            }
            collection.insert_one(document)
            
            connection.disconnect()
        else:
            dispatcher.utter_message("Deu ruim...")

        return []

print("db")