import r2r_dac as r2r
import signal_generator as sg
import time

leds = [16, 20, 21, 25, 26, 17, 27, 22]
amplitude = 3.16
signal_frequency = 5
sampling_frequency = 100
dynamic_range = 3.16

if __name__ == "__main__":
    dac = r2r.R2R_DAC(leds, dynamic_range, True)
    try:
        while True:
            dac.set_voltage(amplitude*sg.get_sin_wave_amplitude(signal_frequency, time.time()))
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()
    