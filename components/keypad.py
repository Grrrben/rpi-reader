from request.req import ApiRequest
from components.led import Led

class Keypad:

    BTN_DASH = "#"  # enter

    BTN_CLEAR = "*"  # Clear

    def __init__(self, logger):
        # a sequence is a list of numbers that make a PIN
        self.sequence = []
        self.logger = logger
        self.api = None

        self._positive_handlers = []
        self._negative_handlers = []


    def input(self, key):
        if key == Keypad.BTN_DASH:
            # this is the enter
            # thus; handle the PIN and clear the sequence afterwards
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

    def register_positive_handler(self, handler):
        self._positive_handlers.append(handler)
    def unregister_positive_handler(self, handler):
        self._positive_handlers.remove(handler)

    def register_negative_handler(self, handler):
        self._negative_handlers.append(handler)
    def unregister_negative_handler(self, handler):
        self._negative_handlers.remove(handler)


    def handle(self):

        key = "".join(self.sequence)
        success = self.api.get_authorized_access_request(key)

        if success:
            for handler in self._positive_handlers:
                handler()
        else:
            for handler in self._negative_handlers:
                handler()

        print(success)

