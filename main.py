import configparser
import logging
from logging.handlers import RotatingFileHandler

from cache.cache import Cache, SimpleCache
from app import App


def init():
    config = configparser.ConfigParser()
    config.read('config.ini')

    logging.basicConfig(
        format='%(levelname)s %(asctime)s: %(message)s',
        level=logging.DEBUG)

    logger = logging.getLogger(__name__)
    handler = RotatingFileHandler('log/rpi_reader_v3.log', maxBytes=2000, backupCount=10)
    logger.addHandler(handler)

    logger.debug("DEBUG in main.init")

    check(config)

    app = App(config)

    if config['default']['use_cache']:
        c = SimpleCache()
        app.set_cache(c)

    app.wait()


def check(config):
    """
    Todo...

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
