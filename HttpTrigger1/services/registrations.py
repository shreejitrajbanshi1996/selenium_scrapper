import json

import HttpTrigger1.config as config
import HttpTrigger1.Util.httpRequest as http
import HttpTrigger1.scrapping.certainScrapper as scrapper


def get_all():
    res = http.get(config.ENTITIES_API["REGISTRATION"])

    return res.json()


def get_all_by_event_id(event_id):

    query = f"$select=*&$filter=_aiad_event_value%20eq%20'{event_id}'"

    res = http.get(f'{config.ENTITIES_API["REGISTRATION"]}?{query}')

    json_data = res.json()

    return json_data["value"]


def create(registrationObj):
    x = json.dumps(registrationObj, indent=4)

    res = http.post(
        config.ENTITIES_API["REGISTRATION"], data=x)

    print(res)


def update(registrationObj):
    x = json.dumps(registrationObj, indent=4)

    res = http.patch(config.ENTITIES_API["REGISTRATION"], data=x)

    print(res)


def get_registration_data_from_certain(username, password, uniqure_report_id):
    data = scrapper.run_scrapper(username, password, uniqure_report_id)

    return data
