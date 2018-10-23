import RPi.GPIO as GPIO
import time

class Buzzer():

    def __init__(self, pin: int):
        self.pin = pin

    def setup(self):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)

    def buzz(self, duration = 0.1):
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(duration)
        GPIO.output(self.pin, GPIO.HIGH)

    def destroy(self):
        GPIO.output(self.pin, GPIO.HIGH)
        GPIO.cleanup()
