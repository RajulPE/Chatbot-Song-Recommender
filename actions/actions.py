# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import webbrowser
import mysql.connector
con=mysql.connector.connect(
        database='songs',
        host='localhost',
        port='3306',
        user='root',
        passwd='mysql',
        auth_plugin='mysql_native_password')

global cursor

class ActionSadSongs(Action):

	def name(self) -> Text:
		return "action_sad"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		cursor = con.cursor()
		query = ("SELECT sad FROM emoSongs")
		cursor.execute(query)
		for(sad) in cursor:
			songString = dispatcher.utter_message("Recommended Song Playlist:{}".format(sad))
			# sadString = (String)sad[2:]
			# print(sad[0])
			webbrowser.open(sad[0])
        # dispatcher.utter_message(text = "playing sad songs")

		return []


class ActionAngerSongs(Action):

	def name(self) -> Text:
		return "action_anger"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		cursor = con.cursor()
		query = ("SELECT anger FROM emoSongs")
		cursor.execute(query)
		for(sad) in cursor:
			songString = dispatcher.utter_message("Recommended Song Playlist:{}".format(sad))
			# sadString = (String)sad[2:]
			print(sad[0])
			webbrowser.open(sad[0])
        # dispatcher.utter_message(text = "playing sad songs")

		return []

class ActionHappySongs(Action):

	def name(self) -> Text:
		return "action_happ"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		cursor = con.cursor()
		query = ("SELECT happy FROM emoSongs")
		cursor.execute(query)
		for(sad) in cursor:
			songString = dispatcher.utter_message("Recommended Song Playlist:{}".format(sad))
			# sadString = (String)sad[2:]
			print(sad[0])
			webbrowser.open(sad[0])
        # dispatcher.utter_message(text = "playing sad songs")

		return []

class ActionSurpriseSongs(Action):

	def name(self) -> Text:
		return "action_surprise"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		cursor = con.cursor()
		query = ("SELECT surprise FROM emoSongs")
		cursor.execute(query)
		for(sad) in cursor:
			songString = dispatcher.utter_message("Recommended Song Playlist:{}".format(sad))
			# sadString = (String)sad[2:]
			print(sad[0])
			webbrowser.open(sad[0])
        # dispatcher.utter_message(text = "playing sad songs")

		return []

class ActionFearSongs(Action):

	def name(self) -> Text:
		return "action_fear"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		cursor = con.cursor()
		query = ("SELECT fear FROM emoSongs")
		cursor.execute(query)
		for(sad) in cursor:
			songString = dispatcher.utter_message("Recommended Song Playlist:{}".format(sad))
			# sadString = (String)sad[2:]
			print(sad[0])
			webbrowser.open(sad[0])
        # dispatcher.utter_message(text = "playing sad songs")

		return []