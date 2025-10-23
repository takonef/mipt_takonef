import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT) # можно настроить все выходы сразу
GPIO.output(leds, 0) # и подать определенный сигнал на все сразу

up = 9
GPIO.setup(up, GPIO.IN)

down = 10
GPIO.setup(down, GPIO.IN)

num = 0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPIO.input(up):
        num = (num+1) % 256
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    
    if GPIO.input(down):
        num = (256 + (num - 1)) % 256
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    for i in range(8):
        GPIO.output(leds[i], dec2bin(num)[i])