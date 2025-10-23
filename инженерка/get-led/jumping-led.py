import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT) # можно настроить все выходы сразу

GPIO.output(leds, 0) # и подать определенный сигнал на все сразу

light_time = 0.1
while True:
    for led in leds:
        GPIO.output(led, 1)
        time.sleep(light_time)
        GPIO.output(led, 0)
    for led in reversed(leds):
        GPIO.output(led, 1)
        time.sleep(light_time)
        GPIO.output(led, 0)