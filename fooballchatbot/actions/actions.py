# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.football import *


class ActionnumGamesPlayed(Action):

    def name(self) -> Text:
        return "action_numGamesPlayed"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = numGamesPlayed(name)

        dispatcher.utter_message(text)

        return []


class ActionwinLossRecord(Action):

    def name(self) -> Text:
        return "action_winLossRecord"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = winLossRecord(name)

        dispatcher.utter_message(text)

        return []


class ActionplayingNow(Action):

    def name(self) -> Text:
        return "action_playingNow"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = playingNow(name)

        dispatcher.utter_message(text)

        return []


class ActionlastOpponent(Action):

    def name(self) -> Text:
        return "action_lastOpponent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = lastOpponent(name)

        dispatcher.utter_message(text)

        return []


class ActionnextOpponent(Action):

    def name(self) -> Text:
        return "action_nextOpponent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = nextOpponent(name)

        dispatcher.utter_message(text)

        return []


class ActionlastScore(Action):

    def name(self) -> Text:
        return "action_lastScore"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = lastScore(name)

        dispatcher.utter_message(text)

        return []


class Actionmanager(Action):

    def name(self) -> Text:
        return "action_manager"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = manager(name)

        dispatcher.utter_message(text)

        return []


class ActionleaguePosition(Action):

    def name(self) -> Text:
        return "action_leaguePosition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = leaguePosition(name)

        dispatcher.utter_message(text)

        return []


class ActionnextGameDate(Action):

    def name(self) -> Text:
        return "action_nextGameDate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = nextGameDate(name)

        dispatcher.utter_message(text)

        return []