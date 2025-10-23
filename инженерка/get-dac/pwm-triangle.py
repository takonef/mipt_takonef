import pwm_dac as pwm
import signal_generator as sg
import time

gpio_pin = 12
amplitude = 3.3
signal_frequency = 10
sampling_frequency = 2000
dynamic_range = 3.3

if __name__ == "__main__":
    dac = pwm.PWM_DAC(gpio_pin, sampling_frequency, dynamic_range, True)
    try:
        while True:
            dac.set_voltage(amplitude*sg.get_triangle_amplitude(signal_frequency, time.time()))
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()
    