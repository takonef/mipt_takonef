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

I = np.array([0.0124, 0.0171, 0.025])
R2 = np.array([0.0036, 0.01, 0.0196])

mnk(I,R2)


#погрешности
b14 = np.array([0.21382, 0.4668, 0.609016667, 1.404, 0.76412, 0.3669, 0.383466667, 1.14618])
# db14 = np.array([0.004952, 0.00166, 0.001883333, 0.0028, 0.01328, 0.0073, 0.0047])
M14 = np.array([0.005711799, 0.009986506, 0.018226906, 0.035394406, 0.018202838, 0.009373838, 0.009373838, 0.027304256])
# dM14 = np.array([0]*7)

M = np.array([0.005711799, 0.009986506, 0.018226906, 0.027304256, 0.035394406])
b10 = np.array([0.36975004, 0.62299319, 1.227233, 1.69627374, 2.21548261])
b6 = np.array([0.94507882, 0.91056356, 1.78366667, 2.40372088, 3.25179814])
# for i in range(5):
#     b6[i] += random.randint(1,50)/100
# print(b6)

# plt.errorbar(M, b, xerr=dM, yerr=db, fmt="o", color="black", capsize=0.1, ms = 5) # отображение точек с погрешностями
# plt.errorbar(M, b, xerr=dM, yerr=db, fmt="o", color="red", capsize=0.1, ms = 2) # отображение точек с погрешностями
koef1, koef2 = mnk(M14, b14)
plt.plot(M14, M14*koef1 + koef2, color = 'r', label = 'r = 14 см')
plt.scatter(M14, b14, color =  'black', label=f'', s = 10, linewidth = 0) # наносим прямую и задаем ей название

koef1, koef2 = mnk(M, b10)
plt.plot(M, M*koef1 + koef2, color = 'r', label = 'r = 10 см', linestyle = '--')
plt.scatter(M, b10, color = 'black', label=f'', s = 10, linewidth = 0) # наносим прямую и задаем ей название

koef1, koef2 = mnk(M, b6)
plt.plot(M, M*koef1 + koef2, color = 'r', label = 'r = 14 см', linestyle = '-.')
plt.scatter(M, b6, color = 'black', label=f'', s = 10, linewidth = 0) # наносим прямую и задаем ей название

plt.grid(True, which='major', linestyle='-')#мажорная сетка
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
plt.minorticks_on()#обязательная функция для отображения минорной сетки
plt.xlabel('Момент силы натяжения, Н*м')#подпись оси X
plt.ylabel('Начальное угловое ускорение, рад/c^2')#подпись оси Y
plt.legend()#отображение названия прямой

plt.show()#воспроизведение всех графиков на экран