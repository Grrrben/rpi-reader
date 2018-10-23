import logging

from cache.cache import Cache
from components.keypad import Keypad
from request.req import ApiRequest

from pad4pi import rpi_gpio
import time


class App():

    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.cache = None

        self.reader_type = config['default']['reader_type']
        self.reader = None

        self.api = ApiRequest(self.config, self.logger)


    def set_cache(self, cache: Cache):
        self.cache = cache

    def wait(self):
        """
        waiting for a signal
        """
        print("I'm listening")

        if self.reader_type == "KEYPAD":

            factory = rpi_gpio.KeypadFactory()
            self.reader = factory.create_4_by_3_keypad()

            kp = Keypad(self.logger)
            kp.set_api(self.api)

            # printKey will be called each time a keypad button is pressed
            self.reader.registerKeyPressHandler(kp.input)

            try:
                while (True):
                    time.sleep(0.1)
            except:
                self.reader.cleanup()

        else:
            self.logger.error("unknown reader")

    def get_cached_access(self, id: int):
        """
        Approve access if the ID has a valid cache
        :param id:
        """
        if self.cache is not None:
            entry = self.cache.get(id)

            if entry:
                # check if now < entry
                pass
