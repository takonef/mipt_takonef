import matplotlib.pyplot as plt
import numpy as np
import random

def mnk(x, y):
    k=(sum(x*y)-sum(x)*sum(y)/len(y))/(sum(x**2)-sum(x)**2/len(y))
    b=(sum(y)-k*sum(x))/len(y)
    sigma_k = (1/(len(x))**0.5)*((sum(y*y)-sum(y)*sum(y)/len(y))/(sum(x*x)-sum(x)*sum(x)/len(y))-k*k)**0.5
    sigma_b = sigma_k*(sum(x*x)-sum(x)*sum(x)/len(x))**0.5
    print("k: ", k, sigma_k, "b: ", b, sigma_b)
    return k, b 

fm = np.array([3.219, 6.083, 9.666, 12.880, 16.104, 19.228, 21.877])
fs = np.array([4.131, 8.276, 12.411, 16.529, 20.681, 25.355, 28.196])
fd = np.array([4.254, 8.497, 12.766, 17.026, 21.535, 24.989, 29.101])
x = np.array([1, 2, 3, 4, 5, 6, 7])

koef1, koef2 = mnk(x, fd)
plt.plot(x, x*koef1 + koef2, color = 'gray', label = 'Дюраль')
plt.scatter(x, fd, color =  'gray', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

koef1, koef2 = mnk(x, fs)
plt.plot(x, x*koef1 + koef2, color = 'black', label = 'Сталь', linestyle = '--')
plt.scatter(x, fs, color = 'black', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

koef1, koef2 = mnk(x, fm)
plt.plot(x, x*koef1 + koef2, color = 'red', label = 'Медь', linestyle = '-.')
plt.scatter(x, fm, color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

plt.grid(True, which='major', linestyle='-')#мажорная сетка
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
plt.minorticks_on()#обязательная функция для отображения минорной сетки
plt.xlabel('Значения n')#подпись оси X
plt.ylabel('Частота резонанса, кГц')#подпись оси Y
plt.legend()#отображение названия прямой

plt.show()#воспроизведение всех графиков на экран