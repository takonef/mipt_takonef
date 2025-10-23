import matplotlib.pyplot as plt
import time

def plot_voltage_vs_time(time, voltage, duration, max_voltage):
    plt.figure(figsize = (10,6))
    plt.plot(time, voltage)

    plt.grid(True, which = 'major', linestyle = '-')
    plt.xlabel("Время, с")
    plt.ylabel("Напражение, В")

    # plt.xlim(duration)
    # plt.ylim(max_voltage)
    plt.show()
def plot_sampling_period_hist(time):
    deltas = []
    for i in range(len(time)-2):
        deltas.append(time[i+1] - time[i])
    
    plt.figure(figsize = (10,6))
    plt.hist(deltas)
    plt.xlabel("Время, с")
    plt.ylabel("Количество измерений")

    plt.grid(True, which = 'major', linestyle = '-')
    plt.show()