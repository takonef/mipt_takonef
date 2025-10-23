import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.leds = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.leds, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.leds, 0)
        GPIO.cleanup

    def number_to_dac(self, number):
        volts = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.leds, volts)
    
    def sequential_counting_adc(self):
        for value in range(256):
            time.sleep(self.compare_time)
            signal = self.number_to_dac(value)
            voltage = (value/256) * self.dynamic_range
            comparatorValue = GPIO.input(self.comp_gpio)
            if comparatorValue:
                # print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
                break
        return value;        

    def successive_approximation_adc(self):
        signal = [0]*8
        for i in signal:
            i = 1
            GPIO.output(self.leds, signal)
            comparatorValue = GPIO.input(self.comp_gpio)
            if comparatorValue:
                i = 0
        
    def get_sc_voltage(self):
        return (self.sequential_counting_adc()/256) * self.dynamic_range


if __name__ == "__main__":
    dynamic_range = 3.2
    try:
        adc = R2R_ADC(dynamic_range)
        while True:
            print(adc.get_sc_voltage())
            time.sleep(0.5)
    finally:
        adc.deinit()
