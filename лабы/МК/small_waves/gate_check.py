import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

while True:
    print(GPIO.input(21))
    time.sleep(0.05)