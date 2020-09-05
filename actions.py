# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionKeralaTotalCases(Action):

    def name(self) -> Text:
        return "action_kerala_total_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        resp = requests.get("https://keralastats.coronasafe.live/summary.json")
        result = resp.json()
        message = "All Kerala Covid numbers as of " + str(result["last_updated"]) + "\n\n"
        keys = ["Hospital Observation", "Home Observation", "Total Observation", "Hospital admitted today", "Confirmed",
                "Recovered", "Deaths", "Active"]
        i = 0
        for key in result["summary"].keys():
            message += keys[i] + " : " + str(result["summary"][key]) + "\n"
            i += 1
        dispatcher.utter_message(text=message)
        return []


class ActionDistrictWiseCases(Action):

    def name(self) -> Text:
        return "action_district_wise_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        district = tracker.get_slot("district")
        resp = requests.get("https://keralastats.coronasafe.live/latest.json")
        result = resp.json()
        keys = ["Hospital Observation", "Home Observation", "Total Observation", "Hospital admitted today", "Confirmed",
                "Recovered", "Deaths", "Active"]
        i = 0
        message = "Covid numbers in " + district + " as of " + str(result["last_updated"]) + "\n\n"
        for key in result["summary"][district].keys():
            message += keys[i] + " : " + str(result["summary"][district][key]) + "\n"
            i += 1

        dispatcher.utter_message(text=message)

        return []


class ActionHotspotsDistrictWise(Action):

    def name(self) -> Text:
        return "action_hotspots_districtwise"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        district = tracker.get_slot("district")
        resp = requests.get("https://keralastats.coronasafe.live/hotspots.json")
        results = resp.json()
        message = ""
        message += "Hotspots in " + district + " as of " + str(results["last_updated"])
        dispatcher.utter_message(text=message)
        message = ""
        count = 0
        for result in results["hotspots"]:
            if result["district"] == district:
                if count >= 10:
                    dispatcher.utter_message(text=message)
                    message = ""
                    count = 0
                else:
                    wards_list = result["wards"].split(",")
                    wards_list = [i.strip() for i in wards_list]
                    wards = ",".join(map(str, wards_list))
                    message += result["lsgd"] + " :  " + "\nwards - " + wards + "\n" + "-" * 49 + "\n"
                    count += 1
        if count < 10:
            dispatcher.utter_message(text=message)
        message = "Last updated : " + str(results["last_updated"])
        dispatcher.utter_message(text=message)

        return []


class ActionButtonDispatch(Action):  # Since FB messenger only allows 3 buttons, telegram uses utter_district_select and fb messenger spits out districs, 3 at a time.

    def name(self) -> Text:
        return "action_district_select_button_dispatch"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        districts = ['Thiruvananthapuram', 'Kollam', 'Alappuzha', 'Pathanamthitta', 'Kottayam', 'Idukki', 'Ernakulam',
                     'Thrissur', 'Palakkad', 'Malappuram', 'Kozhikode', 'Wayanad', 'Kannur', 'Kasaragod']
        input_channel = tracker.get_latest_input_channel()
        i = 0
        if input_channel == "facebook":  # FB allows upto 3 buttons. 14 districts. Adding check to avoid index out of range error at 14
            dispatcher.utter_message(text="Please Select the district.")
            while i < 14:
                if i < 12:
                    dispatcher.utter_message(text="->", buttons=[
                        {"title": districts[i],
                         "payload": "/inform_district{\"district\":" + " \"" + districts[i] + "\"}"},
                        {"title": districts[i + 1],
                         "payload": "/inform_district{\"district\":" + " \"" + districts[i + 1] + "\"}"},
                        {"title": districts[i + 2],
                         "payload": "/inform_district{\"district\":" + " \"" + districts[i + 2] + "\"}"}
                    ])
                else:
                    dispatcher.utter_message(text="->", buttons=[
                        {"title": districts[i],
                         "payload": "/inform_district{\"district\":" + " \"" + districts[i] + "\"}"},
                        {"title": districts[i + 1],
                         "payload": "/inform_district{\"district\":" + " \"" + districts[i + 1] + "\"}"}
                    ])
                i += 3

        else:
            dispatcher.utter_message(template="utter_district_select")
        return []
