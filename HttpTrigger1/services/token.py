import HttpTrigger1.config as config
import HttpTrigger1.Util.httpRequest as http

ACCESS_TOKEN = "access_token"
EXPIRES_IN = "ext_expires_in"


def get_token():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {"grant_type": "client_credentials",
               "client_id": config.CLIENT_ID,
               "client_secret": config.CLIENT_SECRET,
               "resource": config.DYNAMIC_ENV}

    res = http.post(config.AUTH_TOKEN_URL, headers=headers, data=payload)
    res_json = res.json()

    return res_json[ACCESS_TOKEN], res_json[EXPIRES_IN]


def set_token():
    access_token, ext_expires_in = get_token()

    config.TOKEN = access_token
