import RPi.GPIO as GPIO
import time

class Led:
    """
    Class for a RGB led

    __init__ can be used to set pins for the RGB colours. Use the BCM numbering of the GPIO pins.
    See https://pinout.xyz/ for a reference.
    """

    def __init__(self, red = 19, green = 16, blue = 26):
        # Set pins' channels with dictionary, using the BCM numbering as
        # other components (pad4pi) use this mode by default
        self.pins = {'R': red, 'G': green, 'B': blue}

        # Set the GPIO modes to BCM Numbering
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setmode(GPIO.BOARD)
        GPIO.setmode(GPIO.BCM)

        for i in self.pins:
            # set all pins to high 3.3v
            GPIO.setup(self.pins[i], GPIO.OUT, initial=GPIO.HIGH)

        # Setting the led pins as a PWM channel
        self.red = GPIO.PWM(self.pins['R'], 2000)
        self.green = GPIO.PWM(self.pins['G'], 2000)
        self.blue = GPIO.PWM(self.pins['B'], 2000)

        # Setting the led pins as a PWM channel
        self.red.start(0)
        self.green.start(0)
        self.blue.start(0)

    def blink_blue(self, duration = 0.5):
        """ wrapper for a blue blink() """
        self.blink(0, 0, 100, duration)

    def blink_green(self, duration = 0.5):
        """ wrapper for a green blink() """
        self.blink(0, 100, 0, duration)

    def blink_red(self, duration = 0.5):
        """ wrapper for a red blink() """
        self.blink(100, 0, 0, duration)

    def blink(self, r, g, b, duration):
        self.red.ChangeDutyCycle(r)
        self.green.ChangeDutyCycle(g)
        self.blue.ChangeDutyCycle(b)
        time.sleep(duration)
        self.red.ChangeDutyCycle(0)
        self.green.ChangeDutyCycle(0)
        self.blue.ChangeDutyCycle(0)

    def destroy(self):
        # stopping the PWM channels
        self.red.stop()
        self.green.stop()
        self.blue.stop()

        GPIO.output(self.pins, GPIO.HIGH)
        GPIO.cleanup()
