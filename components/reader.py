import RPi.GPIO as GPIO
from components.led import Led
from components.buzzer import Buzzer
import MFRC522
import signal
import time

class Reader():

    continue_reading = True
    
    def scan(self):
        MIFAREReader = MFRC522.MFRC522()
        led = Led()
        led.setup()

        buzzer = Buzzer()
        buzzer.setup()

        # showing a status 
        led.blink_blue(0.1)
        time.sleep(0.1)
        led.blink_blue(0.1)
        time.sleep(0.1)
        led.blink_blue(0.1)

        while self.continue_reading:

            # scanning
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
            (status,uid) = MIFAREReader.MFRC522_Anticoll()

            if status == MIFAREReader.MI_OK:
                led.blink_blue(0.1)
                # for MIFARE with a single UID the UID consists of the first 4 bites. 
                # The fifth one is the Block Check Character, it is calculated as exclusive-or over the 4 previous bytes.
                hex_uid = uid[0:4]
                hex_uid.reverse()

                chip_number = hex_uid[0]<<24 | hex_uid[1]<<16 | hex_uid[2]<<8 | hex_uid[3]

                print "Card read; chip_number %s" % chip_number
                
                try:
                    ok = authenticate(chip_number)
                    if ok:
                        led.blink_green()
                    else:
                        led.blink_red()
                        buzzer.buzz(0.1)
                except Exception as e:
                    print("Exception: %s" % e)
                    led.blink_red(1)
                    buzzer.buzz(0.1)
                    time.sleep(0.2)
                    buzzer.buzz(0.1)
                    # raise e
                    
                
                # # This is the default key for authentication
                # key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
                # MIFAREReader.MFRC522_SelectTag(uid)

                # memory = []
                # for i in range (8):
                #     status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, i, key, uid)
 
                #     # Check if authenticated
                #     if status == MIFAREReader.MI_OK:
                #         memory.append(MIFAREReader.MFRC522_Read(i))

                #     else:

                #         print "Authentication error"
                #         led.blink_red(0.5)
                #         break;
                # else:
                #     led.blink_green(0.2)                 
                # MIFAREReader.MFRC522_StopCrypto1()

    def destroy(self):
        self.continue_reading = False
        GPIO.cleanup()

