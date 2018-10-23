import configparser
import logging

from cache.cache import Cache, SimpleCache
from app import App



def init():
    config = configparser.ConfigParser()
    config.read('config.ini')

    check(config)

    app = App(config)

    if config['default']['use_cache']:
        c = SimpleCache()
        app.set_cache(c)

    app.wait()



def check(config):
    """
    Setup of base values and a test if everything is ready to start the reading functionality.

    Test
    - if required config settings are set
    - if a connection to the server can be made and a token can be acquired

    """

    try:
        if config['default']['reader_type'] not in ("KEYPAD", 'RFID'):
            raise Exception("unknown reader_type {}".format(config['default']['reader_type']))
    except KeyError as e:
        # log
        msg = "missing key in config{}".format(str(e))
        raise


if __name__ == "__main__":
    init()