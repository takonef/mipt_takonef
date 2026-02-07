import numpy as np
import matplotlib.pyplot as plt

cali = np.loadtxt('C:/Users/User/Documents/engineering/engi_takonef/jet/data/cali_0.txt', delimiter = ' ', encoding = 'utf-8')
zero = sum(cali)/len(cali)

zero = 0

cali = np.loadtxt('C:/Users/User/Documents/engineering/engi_takonef/jet/data/cali_100.txt', delimiter = ' ', encoding = 'utf-8')
hundred = sum(cali)/len(cali)

hundred = 913

plt.plot([0, 5], [zero, hundred], label = f'y = {(hundred-zero)/5:.1f}x')
plt.scatter([0, 5], [zero, hundred], color = 'r')
plt.grid(True, which='major', linestyle='-')#мажорная сетка
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
plt.minorticks_on()#обязательная функция для отображения минорной сетки
plt.ylabel('Количество шагов', size = 17)#подпись оси X
plt.xlabel('Расстояниe, см', size = 17)#подпись оси Y
plt.legend(prop={'size': 14})
plt.show()
