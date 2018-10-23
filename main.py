import configparser
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

from cache.cache import Cache, SimpleCache
from app import App

def init():
    config = configparser.ConfigParser()
    config.read('config.ini')

    check(config)

    app = App(config)

    now = datetime.now()
    logfile = "log/smartapi_{0}_{1}.log".format(now.month, now.year)
    file_handler = RotatingFileHandler(logfile, maxBytes=10485760, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

    app.logger.debug("DEBUG in main.init")

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
