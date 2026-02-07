import numpy as np
import matplotlib.pyplot as plt

def centre(x, y):
    for i in range(len(x)):
        if y[i]>1000:
            xo1 = x[i]
            break
    for i in range(xo1, len(x)):
        if y[i]< 1000:
            xo2 = x[i]
            break
    xoxo = x[xo1-2:xo2+2]
    dataxo = y[xo1-2:xo2+2]
    coeffs = np.polyfit(xoxo, dataxo, 2)
    poly = np.poly1d(coeffs)

    max = 0
    ind = 0
    for i in range(len(xoxo)):
        if poly(xoxo)[i] > max:
            max = poly(xoxo)[i]
            ind = i
    x -= xoxo[ind]

def plot(path, dist, l):
    data = np.loadtxt(path, delimiter = ',', encoding = 'utf-8')
    data -= zero

    x = []
    for i in range(len(data)):
        x.append(i)
    x = np.array(x)

    centre(x, data)
    for i in range(len(x)):
        if data[i] < 0:
            data[i] = 0

    x = x*dist/100
    data = data*100/pu
    data = (2*data/1.2)**0.5
    sumo = 0
    for i in range(1, len(x)):
        sumo += abs((abs(x[i]*data[i]) + abs(x[i-1]*data[i-1]))*(x[i]-x[i-1]))/10
    sumo *= 3.14159
    jets.append(float(sumo))
    plt.plot(x, data, label = f'Q({l} см) ={sumo:.2f} г/с')

cali = np.loadtxt('C:/Users/User/Documents/engineering/engi_takonef/jet/data/cali_0.txt', delimiter = ' ', encoding = 'utf-8')
zero = sum(cali)/len(cali)

cali = np.loadtxt('C:/Users/User/Documents/engineering/engi_takonef/jet/data/cali_100.txt', delimiter = ' ', encoding = 'utf-8')
hundred = sum(cali)/len(cali)
pu = hundred - zero

jets = []
plot('C:/Users/User/Documents/engineering/engi_takonef/jet/data/data_0_uh.txt', 1.3, 0)
plot('C:/Users/User/Documents/engineering/engi_takonef/jet/data/data_10_uh.txt', 1.6, 1)
plot('C:/Users/User/Documents/engineering/engi_takonef/jet/data/data_20_uh.txt', 1.7, 2)
plot('C:/Users/User/Documents/engineering/engi_takonef/jet/data/data_30_1.txt', 2.1, 3)
plot('C:/Users/User/Documents/engineering/engi_takonef/jet/data/data_40_1.txt', 2.7, 4)
plot('C:/Users/User/Documents/engineering/engi_takonef/jet/data/data_50_1.txt', 2.5, 5)
plot('C:/Users/User/Documents/engineering/engi_takonef/jet/data/data_60_1.txt', 3.3, 6)
plot('C:/Users/User/Documents/engineering/engi_takonef/jet/data/data_70_2.txt', 2.7, 7)

print(jets)

plt.grid(True, which='major', linestyle='-')#мажорная сетка
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
plt.minorticks_on()#обязательная функция для отображения минорной сетки
plt.ylabel('Скорость воздуха, м/с', size = 17)#подпись оси X
plt.xlabel('Положение трубки Пито относительно струи, см', size = 17)#подпись оси Y
plt.legend(prop={'size': 14})
plt.show()
