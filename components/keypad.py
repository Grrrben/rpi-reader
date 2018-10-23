from request.req import ApiRequest
import logging

class Keypad:

    BTN_DASH = "#"  # enter

    BTN_CLEAR = "*"  # Clear

    def __init__(self):
        # a sequence is a list of numbers that make a PIN
        self.sequence = []
        self.logger = logging.getLogger(__name__)


    def input(self, key):
        if key == Keypad.BTN_DASH:
            # this is the enter
            # thus; handle the PIN and clear the sequence afterwards
            print(self.sequence)
            self.logger.debug("Pin entered {}".format(self.sequence))
            self.handle()
            self.clear()
        elif key == Keypad.BTN_CLEAR:
            self.clear()
        else:
            self.sequence.append(str(key))

    def clear(self):
        """
        empties the sequence
        """
        self.sequence = []

    def set_api(self, api: ApiRequest):

        self.api = api

    def handle(self):

        key = "".join(self.sequence)
        success = self.api.get_authorized_access_request(key)

