import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

file = open('C:/Users/User/Documents/cpp/doubles.csv', 'r')
file1 = open('C:/Users/User/Documents/cpp/floats.csv', 'r')
N=5000
t1=[0]*N
t2=[0]*N
t3=[0]*N
n=[0]*N
inp=file.readline()
inp=file1.readline()
for j in range(0, N):
    inp=file.readline()
    t1[j] = float(inp)
    n[j]=j+1
    # print(t1[j])
for j in range(0, N):
    inp=file1.readline()
    t2[j] = float(inp)

line = [0]*len(t2)
for i in range(len(t2)):
    line[i] = 0.333333333333333333333333333
plt.plot(n, t2, color='blue', label="fl S", linewidth=1)
plt.plot(n, t1, color='red', label="do S", linewidth=1)
plt.plot(n, line, color='green', label="S", linewidth=1)

plt.xlabel("Количество разбиений")##подпись оси абсцисс
plt.ylabel("Значение интеграла")##подпись оси ординат
plt.legend()
plt.grid(True, which='major', linestyle='-')#мажорная сетка
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
plt.minorticks_on()#обязательная функция для отображения минорной сетки
plt.show()