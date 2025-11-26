import numpy as np
import matplotlib.pyplot as plt

def mnk(x, y):
    k=(sum(x*y)-sum(x)*sum(y)/len(y))/(sum(x**2)-sum(x)**2/len(y))
    b=(sum(y)-k*sum(x))/len(y)
    # sigma_k = (1/(len(x))**0.5)*((sum(y*y)-sum(y)*sum(y)/len(y))/(sum(x*x)-sum(x)*sum(x)/len(y))-k*k)**0.5
    # sigma_b = sigma_k*(sum(x*x)-sum(x)*sum(x)/len(x))**0.5
    # print("k: ", k, sigma_k, "b: ", b, sigma_b)
    return k, b 

# # АППРОКСИМАЦИЯ РЕЗУЛЬТАТОВ
# x = np.array([10, 7.4, 6, 4, 2])
# y = np.array([1.38, 1.59, 1.75, 2.15, 3])
# y = (1.32/y)**2

# k, b = mnk(x, y)
# plt.scatter(x, y)
# plt.plot(x, x*k + b, label = 'Линейная аппроксимация квадратов полученных скоростей')
# plt.plot(x, x*9.81/100, label = 'Теоретическая зависимость')

# plt.grid(True, which='major', linestyle='-')#мажорная сетка
# plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
# plt.minorticks_on()#обязательная функция для отображения минорной сетки
# plt.xlabel('Высота воды, см')#подпись оси X
# plt.ylabel('Квадрат скорости, (м/c)^2')#подпись оси Y
# plt.legend()
# plt.show()

# ОБРАБОТКА ЭКСПЕРИМЕНТОВ
data = np.loadtxt('C:/Users/User/Documents/engineering/new-repo/small_waves/expo/expo74.txt', delimiter = ',', encoding = 'utf-8')
time = data[-1] - data[-2]
data = data*7.4/data[0]

x = []
for i in range(len(data)-2):
    x.append(i*time/(len(data)-2))
x = np.array(x)

k1, b1 = mnk(x[0:int(1.5*(len(data)-2)/time)], data[0:int(1.5*(len(data)-2)/time)])
k2, b2 = mnk(x[int(1.5*(len(data)-2)/time):int(2.2*(len(data)-2)/time)], data[int(1.5*(len(data)-2)/time):int(2.2*(len(data)-2)/time)])

plt.plot(x, data[0:-2])
plt.plot(x[0:int(1.7*(len(data)-2)/time)], x[0:int(1.7*(len(data)-2)/time)]*k1 + b1)
plt.plot(x[int(1.45*(len(data)-2)/time):int(2.3*(len(data)-2)/time)], x[int(1.45*(len(data)-2)/time):int(2.3*(len(data)-2)/time)]*k2 + b2, color = 'r')
plt.plot([1.585, 1.585], [3.4, 7.7], label = 't = 1.59 с', linestyle = '--')

plt.grid(True, which='major', linestyle='-')#мажорная сетка
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
plt.minorticks_on()#обязательная функция для отображения минорной сетки
plt.xlabel('Время, с')#подпись оси X
plt.ylabel('Высота воды, см')#подпись оси Y
plt.legend()
plt.show()

# 100 - 1.38
# 74 - 1.59
# 60 - 1.75
# 40 - 2.15
# 20 - 3