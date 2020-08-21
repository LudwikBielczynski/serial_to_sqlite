import time

import RPi.GPIO as GPIO

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)

    try:
        while True:
            for pin in [20, 21, 26]:
                GPIO.output(20, True)
                time.sleep(1)
                GPIO.output(21, False)

    finally:
        GPIO.cleanup()