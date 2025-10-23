import RPi.GPIO as GPIO
import time

class R2R_DAC:
    def __init__(self, leds, dynamic_range, verbose = False):
        self.leds = leds
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.leds, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.leds, 0)
        GPIO.cleanup

    def set_number(self, number):
        volts = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.leds, volts)

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамически диапазон ЦАП (0.00-{self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            number = 0
        number = int(voltage/self.dynamic_range * 255)
        self.set_number(number)

leds = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.16
sleep_time = 0.5

if __name__ == "__main__":
    try:
        dac = R2R_DAC(leds, dynamic_range, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах:"))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз:")
    finally:
        dac.deinit()