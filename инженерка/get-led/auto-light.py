import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

transistor = 6
GPIO.setup(transistor, GPIO.IN)

while True:
    state = not GPIO.input(transistor)
    GPIO.output(led, state)
    time.sleep(0.2)
