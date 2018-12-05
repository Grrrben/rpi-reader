import RPi.GPIO as GPIO
import time

class Relay():

    def __init__(self, pin: int):
        self.pin = pin
        # GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)

    def switch(self, duration = 0.5):
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(duration)
        GPIO.output(self.pin, GPIO.HIGH)

    def destroy(self):
        GPIO.output(self.pin, GPIO.HIGH)
        GPIO.cleanup()
