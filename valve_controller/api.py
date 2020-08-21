import time

import RPi.GPIO as GPIO

RELAY_CHANNELS_BCM_MAP = {1: 26,
                          2: 20,
                          3: 21
                         }

if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    for pin in RELAY_CHANNELS_BCM_MAP.values():
        GPIO.setup(pin, GPIO.OUT)

    print('Setup The Relay Module is successful')
    try:
        while True:
            for channel, pin in RELAY_CHANNELS_BCM_MAP.items():
                GPIO.output(pin, GPIO.LOW)
                print(f'Channel {channel} on pin {pin} is on')
                time.sleep(1)
                GPIO.output(pin, GPIO.HIGH)
    except Exception as message:
        print(f'An exception occurred: {message}')

    finally:
        GPIO.cleanup()