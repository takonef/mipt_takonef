import RPi.GPIO as GPIO
import time
import smbus as i2c
class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = i2c.SMBus(1)
        self.verbose = verbose
        self.dynamic_range=dynamic_range
        self.address=0x4D
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные {data}, старший бит {upper_data_byte}, младший бит {lower_data_byte}, число {number}")
        return number    
    def get_voltage(self):
        return self.get_number()/1023*self.dynamic_range

if (__name__ == "__main__"):
    try:
        adc=MCP3021(5.18)
        while True:
            V=adc.get_voltage()
            print(V)
            time.sleep(1)
            
    finally:
        adc.deinit()