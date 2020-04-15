# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_core_sdk import Action

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


from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionCheckWeather(Action):
   def name(self) -> Text:
      return "action_check_weather"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      dispatcher.utter_message("Hello World! from custom action")
      return []


import requests
import json



class ApiAction(Action):
   def name(self):
      return "action_retrieve_image"

   def run(self, dispatcher, tracker, domain):
      group = tracker.get_slot('group')

      r = requests.get('http://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(group))
      response = r.content.decode()
      response = response.replace('["', "")
      response = response.replace('"]', "")

      # display(Image(response[0], height=550, width=520))
      dispatcher.utter_message("Here is something to cheer you up: {}".format(response))


class ActionGetNewst(Action):

   def name(self):
      return 'action_get_news'

   def run(self, dispatcher, tracker, domain):
      category = tracker.get_slot('category')
      print(category)
      url = 'https://api.nytimes.com/svc/news/v3/content/all/{category}.json'.format(category=category)
      params = {'api-key': "YwFABCbVPDGGaM7aNgXuPdlPt2DuEK6I", 'limit': 5}
      response = requests.get(url, params).text
      json_data = json.loads(response)['results']
      i = 0
      for results in json_data:
         i = i + 1
         message = str(i) + "." + results['abstract']
         dispatcher.utter_message(message)
      return []
