import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('C:/Users/User/Documents/engineering/mipt_takonef/2beat2.txt', delimiter = ' ')

print(data)

x = data[0::]
y = data[1:]

# print(y)s

# # plt.plot(x, data, label = f'Q({l} см) ={sumo:.2f} г/с')

# plt.grid(True, which='major', linestyle='-')#мажорная сетка
# plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
# plt.minorticks_on()#обязательная функция для отображения минорной сетки
# plt.ylabel('Скорость воздуха, м/с', size = 17)#подпись оси X
# plt.xlabel('Положение трубки Пито относительно струи, см', size = 17)#подпись оси Y
# plt.legend(prop={'size': 14})
# plt.show()