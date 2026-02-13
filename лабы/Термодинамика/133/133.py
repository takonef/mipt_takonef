import matplotlib.pyplot as plt
import numpy as np
import random
import math
from scipy.optimize import curve_fit


def mnk(x, y):
    k=(sum(x*y)-sum(x)*sum(y)/len(y))/(sum(x**2)-sum(x)**2/len(y))
    b=(sum(y)-k*sum(x))/len(y)
    sigma_k = (1/(len(x))**0.5)*((sum(y*y)-sum(y)*sum(y)/len(y))/(sum(x*x)-sum(x)*sum(x)/len(y))-k*k)**0.5
    sigma_b = sigma_k*(sum(x*x)-sum(x)*sum(x)/len(x))**0.5
    print("k: ", k, sigma_k, "b: ", b, sigma_b)
    return k, b

def root_func(x, a, b):
    return a * np.sqrt(x) + b

V1 = np.array([0.5, 0.5, 1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5])
t1 = np.array([74.66, 39.93, 40.07, 27.42, 41.05, 50.18, 42.31, 37.16, 33.18, 41.91, 49.07, 47.06, 45.45, 43.69, 40.6, 36.41])
dP1 = np.array([5, 10, 20, 30, 41, 50, 60, 71, 82, 91, 106, 125, 140, 165, 190, 240])

V2 = np.array([0.604, 0.501, 1.5, 1.5, 3, 3, 5, 5, 5, 5, 5, 7.501, 7.501, 7.501, 7.501, 7.501])
t2 = np.array([35.32, 21.37, 37.55, 21.57, 30.79, 25.03, 33.56, 29.54, 27.89, 26.48, 25.29, 36.73, 35.65, 34.63, 33.76, 32.25])
dP2 = np.array([5, 10, 20, 41, 60, 79, 101, 120, 130, 140, 150, 160, 170, 180, 191, 210])

V3 = np.array([0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 2.5, 3, 3, 3, 5, 5, 5, 5, 8, 8])
t3 = np.array([40.31, 19.77, 39.92, 30.37, 23.20, 20.34, 29.56, 28.54, 25.58, 23.84, 35.92, 33.79, 31.27, 27.64, 38.24, 36.18])
dP3 = np.array([2, 5, 8, 11, 15, 17, 20, 25, 30, 35, 40, 50, 65, 85, 110, 121])


for i in range(len(V1)):
    V1[i] = (V1[i]/t1[i])
    dP1[i] = dP1[i]

for i in range(len(V2)):
    V2[i] = (V2[i]/t2[i])
    dP2[i] = dP2[i]

for i in range(len(V3)):
    V3[i] = (V3[i]/t3[i])
    dP3[i] = dP3[i]


# dP1 = dP1
# dP1 = np.log(dP1)
# V1 = V1
# V1 = V1
# V1 = np.log(V1)

# dP2 = dP2
# dP2 = np.log(dP2)
# V2 = V2
# V2 = V2
# V2 = np.log(V2)

# dP3 = dP3
# dP3 = np.log(dP3)
# V3 = V3
# V3 = V3
# V3 = np.log(V3)


# V1 = V1[8:]
# dP1 = dP1[8:]
# V2 = V2[8:]
# dP2 = dP2[8:]
# V3 = V3[8:]
# dP3 = dP3[8:]
'''
plt.errorbar(dP1, V1, xerr=0, fmt='+', color='red', ms = 10, capsize=5, linewidth = 0, label='d = 3.90 мм')
k, b = mnk(dP1, V1)
plt.plot(dP1, k*dP1 + b, color = 'blue', label=r'ln(Q) = 0.364 $\cdot$ x - 3.99', linewidth = 1) # наносим прямую и задаем ей название

plt.errorbar(dP2, V2, xerr=0, fmt='x', color='green', ms = 10, capsize=5, linewidth = 0, label='d = 3.90 мм')
k, b = mnk(dP2, V2)
plt.plot(dP2, k*dP2 + b, color = 'blue', label=r'ln(Q) = 0.533 $\cdot$ x - 4.30', linewidth = 1, linestyle='-.') # наносим прямую и задаем ей название

plt.errorbar(dP3, V3, xerr=0, fmt='o', color='blue', ms = 10, capsize=5, linewidth = 0, label='d = 3.90 мм')
k, b = mnk(dP3, V3)
plt.plot(dP3, k*dP3 + b, color = 'blue', label=r'Q = 0.433 $\cdot$ x - 3.61', linewidth = 1, linestyle='--') # наносим прямую и задаем ей название




for i in range(len(V1)):
    V1[i] = (V1[i]/t1[i])*1000
    dP1[i] = dP1[i]*3.92

for i in range(len(V2)):
    V2[i] = ((V2[i]/t2[i])/2.5)*1000
    dP2[i] = dP2[i]*3.92

for i in range(len(V3)):
    V3[i] = (V3[i]/t3[i])*1000
    dP3[i] = dP3[i]*3.92

# plt.scatter(dP1[0:8], V1[0:8], color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

# plt.errorbar(dP1, V1, xerr=2, fmt='+', color='red', ms = 10, capsize=5, linewidth = 0, label='d = 3.90 мм')
# k, b = mnk(dP1[0:8], V1[0:8])
# plt.plot(dP1[0:12], k*dP1[0:12] + b, color = 'blue', label=r'Q = 0.290 $\cdot$ x + 1.89', linewidth = 1) # наносим прямую и задаем ей название
# popt, pcov = curve_fit(root_func, dP1[8:], V1[8:])
# perr = np.sqrt(np.diag(pcov))
# print(perr)
# a_fit, b_fit = popt
# print(f"Аппроксимированная функция: {a_fit:.3f} * sqrt(x + {b_fit:.3f})")
# plt.plot(dP1, root_func(dP1, *popt), 'blue', label=r'Q = 3.47 $\cdot$ sqrt(x + 29.3)', linestyle= '--' )
# plt.scatter([301.6], [89.4], color='blue', label='P = 301.6, Q = 89.4', s = 60)   


# plt.errorbar(dP2, V2, xerr=2, fmt='+', color='red', ms = 8, capsize=5, linewidth = 0, label='d = 3.0 мм')
# k, b = mnk(dP2[0:8], V2[0:8])
# plt.plot(dP2[0:12], k*dP2[0:12] + b, color = 'blue', label=r'Q = 0.134 $\cdot$ x + 5.10', linewidth = 1) # наносим прямую и задаем ей название
# popt, pcov = curve_fit(root_func, dP2[8:], V2[8:])
# perr = np.sqrt(np.diag(pcov))
# print(perr)
# a_fit, b_fit = popt
# a_fit, b_fit = popt
# print(f"Аппроксимированная функция: {a_fit:.3f} * sqrt(x + {b_fit:.3f})")
# plt.plot(dP2, root_func(dP2, *popt), 'b', label=r'Q = 3.42 $\cdot$ sqrt(x - 4.58)',)
# plt.scatter([473.5], [69.9], color='blue', label='P = 473.5, Q = 69.9', s = 60)   


# plt.errorbar(dP3, V3, xerr=2, fmt='+', color='red', ms = 10, capsize=5, linewidth = 0, label= 'd = 5.10 мм')
# k, b = mnk(dP3[0:8], V3[0:8])
# plt.plot(dP3[0:12], k*dP3[0:12] + b, color = 'blue', label=r'Q = 1.016 $\cdot$ x + 5.79', linewidth = 1) # наносим прямую и задаем ей название
# popt, pcov = curve_fit(root_func, dP3[8:], V3[8:])
# perr = np.sqrt(np.diag(pcov))
# print(perr)
# a_fit, b_fit = popt
# print(f"Аппроксимированная функция: {a_fit:.3f} * sqrt(x + {b_fit:.3f})")
# plt.plot(dP3, root_func(dP3, *popt), 'blue', label=r'Q = 9.06 $\cdot$ sqrt(x + 20.3)', linestyle= '--' )
# plt.scatter([106.2], [113.5], color='blue', label='P = 106.2, Q = 113.5', s = 60)   


# plt.scatter(dP2[0:8], V2[0:8], color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название
# plt.scatter(dP3[0:8], V3[0:8], color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название
# k, b = mnk(dP2[0:8], V2[0:8])
# plt.plot(dP2[0:8], k*dP2[0:8] + b, color = 'blue', label=f'', linewidth = 1) # наносим прямую и задаем ей название
# k, b = mnk(dP3[0:8], V3[0:8])
# plt.plot(dP3[0:8], k*dP3[0:8] + b, color = 'blue', label=f'', linewidth = 1) # наносим прямую и задаем ей название


# plt.scatter(dP1[:9], (V1/(3.14159*(0.198*0.198)))[:9], color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

# plt.scatter(dP1[9:], (V1/(3.14159*(0.198*0.198)))[9:], color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

# plt.scatter(dP3, V3/(3.14159*0.15*0.15), color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

# k, b = mnk(dP3[0:8], (V3/(3.14159*0.15*0.15))[0:8])
# plt.plot(dP3, k*dP3 + b, color = 'blue', label=f'', linewidth = 1) # наносим прямую и задаем ей название

# plt.scatter(dP3, V3/(3.14159*2.55*2.55), color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

# plt.scatter(dP2, V2*V2, color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название


'''

# #---------------
# Ps1 = np.array([65, 130, 174, 109, 62, 46])
# ls1 = [50, 90, 120, 70, 40, 30]


Ps1 = np.array([2.72/60, 2.39/60, 3.88/60])
ls1 = np.array([3.9, 3.0, 5.1])
plt.scatter(np.log(ls1), np.log(Ps1), color = 'green', label=f'', s = 30, linewidth = 0)
k, b = mnk(np.log(ls1), np.log(Ps1))
plt.plot(ls1, k*ls1 + b, color = 'blue', label=r'ln(Q) = 0.533 $\cdot$ x - 4.30', linewidth = 1, linestyle='-.') # наносим прямую и задаем ей название
# Ps2 = np.array([239, 117, 300, 184])
# ls2 = [50, 20, 31, 11]
# plt.scatter(ls2, Ps2*3.92, color = 'red', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

# Ps3 = np.array([25, 46, 67, 41, 18, 22])
# ls3 = [50, 90, 120, 70, 40, 30]
# plt.scatter(ls3, Ps3*3.92, color = 'blue', label=f'', s = 30, linewidth = 0) # наносим прямую и задаем ей название

plt.grid(True, which='major', linestyle='-')#мажорная сетка
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
plt.minorticks_on() #обязательная функция для отображения минорной сетки
plt.xlabel('Логарифм перепада давления, ln(Па)', fontsize=20) #подпись оси X
plt.ylabel(r'Логарифм реднего расхода, ln(м/с $\cdot$ 10^-6)', fontsize=20) #подпись оси Y
plt.legend(fontsize=20)#отображение названия прямой

plt.show()#воспроизведение всех графиков на экран

