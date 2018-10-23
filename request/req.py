from urllib.parse import urlencode
from urllib.request import Request, urlopen
from http import client
import json
from datetime import datetime
import dateutil.parser


class ApiRequest():

    def __init__(self, config):
        self.token = ""
        self.expires_at = datetime.now()
        self.config = config

    def get_token(self):

        if self.token != "" and self.expires_at > datetime.now():
            # no need to renew
            return self.token

        email = self.config['default']['username']
        password = self.config['default']['password']

        # login with Runremote rights
        params = urlencode({
            'email': email,
            'password': password
        })
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }
        conn = client.HTTPConnection(self.config['default']['api_url'])
        conn.request("POST", self.config['default']['endpoint_token'], params, headers)

        # fetch token from response
        response = conn.getresponse()
        data = json.loads(response.read())

        # setting the tokens in
        self.token = data["token"]
        self.expires_at = dateutil.parser.parse(data["expiresAt"])

        return self.token


    def get_authorized_access_request(self, url: str) -> bool:

        headers = {
            "Authorization": "Bearer %s".format(self.get_token())
        }

        request = Request(url, headers=headers)
        jsonRequest = urlopen(request).read().decode()

        if "error" in jsonRequest:
            print(jsonRequest["error"])
            return False

        if "success" in jsonRequest:
            success = jsonRequest["success"]
            return success



        print(jsonRequest)
        print(type(jsonRequest))

