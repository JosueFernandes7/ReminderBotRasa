# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionTarefa(Action):
    def name(self):
        return 'action_salvar_tarefa'

    def run(self, dispatcher, tracker, domain):

        nome_usuario = tracker.get_slot('nome_usuario')
        nome_tarefa = tracker.get_slot('nome_tarefa')

        if nome_tarefa and nome_usuario:
            dispatcher.utter_message(f"Tarefa: {nome_tarefa}\nUsuário: {nome_usuario}")
        else:
            dispatcher.utter_message("Deu ruim...")

        return []

def autenticar_usuario(nome, senha):
    
    return False