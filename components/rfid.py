from request.req import ApiRequest
from pirc522 import RFID


class Rfid:
    def __init__(self, logger):
        self.logger = logger
        self.api = None
        self.rdr = None

        self._positive_handlers = []
        self._negative_handlers = []

    def set_api(self, api: ApiRequest):
        self.api = api

    def register_positive_handler(self, handler):
        """
        Registers a handler (function) that will be called when a positive action is performed e.g. Access granted
        There can be any number of handlers
        """
        self._positive_handlers.append(handler)

    def unregister_positive_handler(self, handler):
        """
        Removes a handler from the positive handler list
        """
        self._positive_handlers.remove(handler)

    def register_negative_handler(self, handler):
        """
        Registers a handler (function) that will be called when a negative action is performed e.g. Access denied
        There can be any number of handlers
        """
        self._negative_handlers.append(handler)

    def unregister_negative_handler(self, handler):
        """
        Removes a handler from the positive handler list
        """
        self._negative_handlers.remove(handler)

    def wait(self):
        """
        Waiting for a signal
        """

        self.rdr = RFID()

        while True:
            self.rdr.wait_for_tag()
            (error, tag_type) = self.rdr.request()
            if not error:
                print("Tag detected")
                (error, uid) = self.rdr.anticoll()
                if not error:
                    print("UID: " + str(uid))
                    # Select Tag is required before Auth
                    if not self.rdr.select_tag(uid):
                        # Auth for block 10 (block 2 of sector 2) using default shipping key A
                        if not self.rdr.card_auth(self.rdr.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
                            # This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                            print("Reading block 10: " + str(self.rdr.read(10)))
                            # Always stop crypto1 when done working
                            self.rdr.stop_crypto()

    def destroy(self):
        # Calls GPIO cleanup
        self.rdr.cleanup()
