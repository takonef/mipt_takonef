import RPi.GPIO as GPIO
import mcp3021_driver as MCP
import adc_plot
import time
import numpy as np

# 132 см
GPIO.setmode(GPIO.BCM)
gate = 15
comp = 21
GPIO.setup(gate, GPIO.IN)
GPIO.setup(comp, GPIO.IN)

dynamic_range = 5.18
while GPIO.input(21):
    time.sleep(0.05)
       
mcp = MCP.MCP3021(dynamic_range)
try:
    height = mcp.get_voltage()
    cur = height
    volts = []
    volts.append(height)
    start_time = time.time()
    while(cur*2 > height):
        cur = mcp.get_voltage()
        volts.append(cur)
    end_time = time.time()
    volts.append(start_time)
    volts.append(end_time)
    np.savetxt('exp20.txt', volts, delimiter = ',', fmt = '%.4f', header = 'Время[c], Напряжение[B]', comments ='', encoding = 'utf-8')

finally:
    mcp.deinit()