from http import client
import json
from datetime import datetime
import dateutil.parser
from urllib import request, parse
import json


class ApiRequest():

    def __init__(self, config):
        self.token = ""
        self.expires_at = datetime.now()
        self.config = config

    def get_token(self):

        print("getting token")

        if self.token != "" and self.expires_at > datetime.now():
            # no need to renew
            return self.token

        email = self.config['default']['username']
        password = self.config['default']['password']

        # login with Runremote rights
        params = parse.urlencode({
            'email': email,
            'password': password
        }).encode()

        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }
        url = "{}{}".format(self.config['default']['api_url'], self.config['default']['endpoint_token'])
        req = request.Request(url, data = params, headers=headers)
        resp = request.urlopen(req)
        data = json.loads(resp.read())

        # setting the tokens in
        self.token = data["token"]
        self.expires_at = dateutil.parser.parse(data["expiresAt"])

        return self.token


    def get_authorized_access_request(self, key: str) -> bool:

        headers = {
            "Authorization": "Bearer %s".format(self.get_token())
        }

        url = self.config['default']['endpoint_access'].format(
            device_id=self.config['default']['reader_id'], identifier=key)

        print(url)

        request = Request(url, headers=headers)
        jsonRequest = urlopen(request).read().decode()

        print(jsonRequest)
        print(type(jsonRequest))

        if "error" in jsonRequest:
            print(jsonRequest["error"])
            return False

        if "success" in jsonRequest:
            success = jsonRequest["success"]
            return success
