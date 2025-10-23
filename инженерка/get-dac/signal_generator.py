import time
import math

def get_sin_wave_amplitude(freq, time):
    y = math.sin(2*3.14149*freq*time)
    print((y+1)/2)
    return (y + 1)/2

def get_triangle_amplitude(freq, time):
    T = 1/freq
    sig = time%T
    if sig < T/2:
        return 10*(time%T) 
    return 10*(T - time%T)

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)