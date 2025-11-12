import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def mnk(x, y):
    k=(sum(x*y)-sum(x)*sum(y)/len(y))/(sum(x**2)-sum(x)**2/len(y))
    b=(sum(y)-k*sum(x))/len(y)
    sigma_k = (1/(len(x))**0.5)*((sum(y*y)-sum(y)*sum(y)/len(y))/(sum(x*x)-sum(x)*sum(x)/len(y))-k*k)**0.5
    sigma_b = sigma_k*(sum(x*x)-sum(x)*sum(x)/len(x))**0.5
    print("k: ", k, sigma_k, "b: ", b, sigma_b)
    return k, b 

P = np.array([4.990347, 9.929682, 14.797404, 19.731834, 24.636834, 29.270097, 33.800355])
N = np.array([0, 2.825, 5.53, 8.32, 11.22, 13.83, 16.36])
koef1, koef2 = mnk(P, N)
plt.plot(P, P*koef1 + koef2, color = 'r', label = 'линейная аппроксимация')
plt.scatter(P, N, color =  'black', label=f'', s = 20, linewidth = 0) # наносим прямую и задаем ей название

plt.grid(True, which='major', linestyle='-')#мажорная сетка
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
plt.minorticks_on()#обязательная функция для отображения минорной сетки
plt.xlabel('P, Н')#подпись оси X
plt.ylabel('n, мм')#подпись оси Y
plt.legend()#отображение названия прямой

plt.show()#воспроизведение всех графиков на экран

# file = open('C:/Users/User/Documents/cpp/doubles.csv', 'r')
# file1 = open('C:/Users/User/Documents/cpp/floats.csv', 'r')
# N=5000
# t1=[0]*N
# t2=[0]*N
# t3=[0]*N
# n=[0]*N
# inp=file.readline()
# inp=file1.readline()
# for j in range(0, N):
#     inp=file.readline()
#     t1[j] = float(inp)
#     n[j]=j+1
#     # print(t1[j])
# for j in range(0, N):
#     inp=file1.readline()
#     t2[j] = float(inp)

# line = [0]*len(t2)
# for i in range(len(t2)):
#     line[i] = 0.333333333333333333333333333
# plt.plot(P, t2, color='blue', label="fl S", linewidth=1)
# plt.plot(n, t1, color='red', label="do S", linewidth=1)
# plt.plot(n, line, color='green', label="S", linewidth=1)

# plt.xlabel("Количество разбиений")##подпись оси абсцисс
# plt.ylabel("Значение интеграла")##подпись оси ординат
# plt.legend()
# plt.grid(True, which='major', linestyle='-')#мажорная сетка
# plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
# plt.minorticks_on()#обязательная функция для отображения минорной сетки
# plt.show()