import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 5
signal_frequency = 10
sampling_frequency = 1000
dynamic_range = 5.18

if __name__ == "__main__":
    dac = mcp.MCP4725(dynamic_range)
    try:
        while True:
            dac.set_voltage(amplitude*sg.get_triangle_amplitude(signal_frequency, time.time()))
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()