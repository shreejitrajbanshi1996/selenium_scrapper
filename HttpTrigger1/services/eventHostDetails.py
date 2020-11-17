import HttpTrigger1.config as config
import HttpTrigger1.Util.httpRequest as http


def get_partner_credential():
    url = config.ENTITIES_API["EVENT_HOST_DETAILS"]

    print(url)
    res = http.get(url)

    json_data = res.json()

    event_host_detail = json_data["value"][0]

    return event_host_detail["aiad_certainusename"], event_host_detail["aiad_certainpassword"]
