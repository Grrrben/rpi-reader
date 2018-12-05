import logging
import time

from pad4pi import rpi_gpio

from app.components import *
from app.cache.cache import *
from app.request.req import ApiRequest


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

        led = Led()
        led.blink_blue()

        relay = Relay(6)

        if self.reader_type == "KEYPAD":

            factory = rpi_gpio.KeypadFactory()

            keypad = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                ["*", 0, "#"]
            ]
            row_pins = [4, 14, 15, 17]  # BCM numbering
            col_pins = [18, 27, 22]  # BCM numbering

            self.reader = factory.create_keypad(keypad=keypad, row_pins=row_pins, col_pins=col_pins)

            kp = Keypad(self.logger)
            kp.set_api(self.api)

            kp.register_positive_handler(led.blink_green)
            kp.register_negative_handler(led.blink_red)

            # printKey will be called each time a keypad button is pressed
            self.reader.registerKeyPressHandler(kp.input)

            try:
                while (True):
                    time.sleep(0.1)
            except:
                self.reader.cleanup()
        elif self.reader_type == "RFID":

            rfid = Rfid(self.logger)
            rfid.set_api(self.api)

            rfid.register_positive_handler(led.blink_green)
            rfid.register_positive_handler(relay.switch)
            rfid.register_negative_handler(led.blink_red)

            rfid.wait()

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
