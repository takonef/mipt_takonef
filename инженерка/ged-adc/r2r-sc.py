import r2r_adc
import time
import adc_plot

dynamic_range = 3.2
adc = r2r_adc.R2R_ADC(dynamic_range)
voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()
    while (time.time() - start_time) < duration:
        time_values.append(time.time()-start_time)
        voltage_values.append(adc.get_sc_voltage())
    print(time_values, voltage_values)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, duration, dynamic_range)
    adc_plot.plot_sampling_period_hist(time_values)
    
finally:
    adc.deinit()