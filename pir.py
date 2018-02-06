import RPi.GPIO as GPIO
import time
import urllib

DOMOTICZ_SWITCH_ID = 1
DOMOTICZ_SWITCH_URL = "http://127.0.0.1:8080/json.htm?type=command&param=switchlight&idx={0}&switchcmd=On".format(DOMOTICZ_SWITCH_ID)
PIR_STATE_FILE = "pirstate.txt"
GPIO.setmode(GPIO.BCM)
PIR_PIN = 23
GPIO.setup(PIR_PIN, GPIO.IN)

previous_state = False
current_state = False

try:
    print("PIR Module Started (CTRL+C to exit)")
    time.sleep(2)
    print("PIR Ready")
    while True:
        time.sleep(0.2)
        previous_state = current_state
        current_state = GPIO.input(PIR_PIN)
        if current_state != previous_state:
            print("Motion Detected!")
            httpresponse = urllib.urlopen (DOMOTICZ_SWITCH_URL)
            print(httpresponse.read())
        with open(PIR_STATE_FILE, 'w') as file:
            file.write("{0}".format(current_state))
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
