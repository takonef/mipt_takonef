import RPi.GPIO as GPIO
import time

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        GPIO.setmode(GPIO.BCM)
        
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 1)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        duty = 0.0
        self.pwm.start(duty)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамически диапазон ЦАП (0.00-{self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            duty = 0.0
        duty = int(voltage/self.dynamic_range * 100)
        self.pwm.ChangeDutyCycle(duty)
        print(f"Коэффициент заполнения: {duty}")

gpio_pin = 12
frequency = 500
dynamic_range = 3.3
sleep_time = 0.5

if __name__ == "__main__":
    dac = PWM_DAC(gpio_pin, frequency, dynamic_range, True)
    try:
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах:"))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз:")
    finally:
        dac.deinit()