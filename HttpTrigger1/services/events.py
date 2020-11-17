import json

import HttpTrigger1.config as config
import urllib
import HttpTrigger1.Util.httpRequest as http
import HttpTrigger1.const.fields.events as event_fields


def get_all_valid_events():
    events_url = config.ENTITIES_API["EVENTS"]
    query = f"$select=*"
    url = f"{events_url}?{query}"

    print(url)
    res = http.get(url)

    json_data = res.json()

    return json_data["value"]


def get_by_certain_unique_report_id(unique_report_id):
    events_url = config.ENTITIES_API["EVENTS"]
    encoded_report_id = urllib.parse.quote(unique_report_id)
    query = f"$select=*&$filter={event_fields.UNIQUE_REGISTRATION_ID}%20eq%20'{encoded_report_id}'"
    url = f"{events_url}?{query}"

    print(url)
    res = http.get(url)

    print(res.json())
