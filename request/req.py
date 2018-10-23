from urllib import request, parse
from urllib.error import HTTPError
from datetime import datetime, timezone
import dateutil.parser
import json


class ApiRequest():

    def __init__(self, config, logger):
        self.token = ""
        self.expires_at = datetime.now(timezone.utc)
        self.config = config
        self.logger = logger

    def get_token(self):

        print("getting token")

        if self.token != "" and self.expires_at > datetime.now(timezone.utc):
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
        data = json.loads(resp.read().decode('utf-8'))

        # setting the tokens in
        self.token = data["token"]
        self.expires_at = dateutil.parser.parse(data["expiresAt"])

        return self.token


    def get_authorized_access_request(self, key: str) -> bool:

        headers = {
            "Authorization": "Bearer {}".format(self.get_token())
        }

        path = self.config['default']['endpoint_access'].format(
            device_id=self.config['default']['reader_id'], identifier=key)

        url = "{}{}".format(self.config['default']['api_url'], path)

        try:
            req = request.Request(url, headers=headers)
            resp = request.urlopen(req)
            data = json.loads(resp.read().decode('utf-8'))

            print(data)
            print(type(data))

            if "error" in data:
                self.logger.error(data["error"])
                return False

            if "success" in data:
                success = data["success"]
                return success
        except HTTPError as e:
            self.logger.error(str(e))
            return False
