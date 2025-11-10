import mcp3021_driver
import time
import adc_plot

dynamic_range = 5.18
adc = mcp3021_driver.MCP3021(dynamic_range)
voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()
    while (time.time() - start_time) < duration:
        time_values.append(time.time()-start_time)
        voltage_values.append(adc.get_voltage())
    print(time_values, voltage_values)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, duration, dynamic_range)
    adc_plot.plot_sampling_period_hist(time_values)
    
finally:
    adc.deinit()