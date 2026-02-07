import matplotlib.pyplot as plt
import numpy as np
import random

V = np.array([0.5, 0.5, 1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5])
t = np.array([74.66, 39,93, 40.07, 27.42, 41.05, 50.18, 42.31, 37.16, 33.18, 41.91, 49.07, 47.06, 45.45, 43.69, 40.6, 36.41])
dP = np.array([5, 10, 20, 30, 41, 50, 60, 71, 82, 91, 106, 125, 140, 165, 190, 240])

for i in range(len(V)):
    V[i] = V[i]/t[i]

plt.scatter(dP, V, color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

plt.grid(True, which='major', linestyle='-')#мажорная сетка
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
plt.minorticks_on()#обязательная функция для отображения минорной сетки
plt.xlabel('Значения n')#подпись оси X
plt.ylabel('Частота резонанса, кГц')#подпись оси Y
plt.legend()#отображение названия прямой

plt.show()#воспроизведение всех графиков на экран