import RPi.GPIO as GPIO
import time
import smbus

class MCP4725:
    def __init__(self, dynamic_range, address = 0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа.")
        
        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4752 (12 бит)")
        
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамически диапазон ЦАП (0.00-{self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            volts = 0.0
        volts = int(voltage/self.dynamic_range * 4095)
        self.set_number(volts)

dynamic_range = 5.18
sleep_time = 0.5

if __name__ == "__main__":
    dac = MCP4725(dynamic_range)
    try:
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах:"))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз:")
    finally:
        dac.deinit()