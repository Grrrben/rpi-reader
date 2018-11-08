import configparser
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler

import RPi.GPIO as GPIO

from app import App
from app.cache import SimpleCache

app = None

def init():
    config = configparser.ConfigParser()
    config.read('config.ini')

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

def destroy():
    """ ending the program gracefully """
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        init()

    # Cleaning GPIO up when 'Ctrl+C' is pressed
    except KeyboardInterrupt:
        destroy()
