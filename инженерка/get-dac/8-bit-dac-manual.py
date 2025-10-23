import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(leds, GPIO.OUT) # можно настроить все выходы сразу
GPIO.output(leds, 0) # и подать определенный сигнал на все сразу

dynamic_range = 3.16
def voltage_to_number(voltage):

    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамически диапазон ЦАП (0.00-{dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage/dynamic_range * 255)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.5
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах:"))
            number = voltage_to_number(voltage)
            volts = dec2bin(number)
            print(f"Число на вход ЦАП: {number}, биты {volts}")
            GPIO.output(leds, volts)
            time.sleep(sleep_time)

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз:")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()