import matplotlib.pyplot as plt

M = 1.989 * (10**30)
G = 6.67 * (10**(-11))
T = 3*365*24*60*60 # year
dt = 100 # hours

Vx = 0  
Vy = 30000 #km/s
x = 147*10**9  # m
y = 0

ax = -(G*M/((x*x + y*y)**1.5))*x
ay = 0

X = []
Y = []

for i in range(T//dt):
    X.append(x)
    Y.append(y)
    
    Vx = Vx + ax*dt
    ax = -(G*M/((x*x + y*y)**1.5))*x
    x = x + Vx*dt
    
    Vy = Vy + ay*dt
    ay = -(G*M/((x*x + y*y)**1.5))*y
    y = y + Vy*dt
    
plt.scatter(X, Y, color = 'red', label=f'', s = 3, linewidth = 0) # наносим прямую и задаем ей название

plt.grid(True, which='major', linestyle='-')#мажорная сетка
plt.grid(True, which='minor', linestyle='--', linewidth=0.5)#минорная сетка
plt.minorticks_on()#обязательная функция для отображения минорной сетки
# plt.xlabel('Значения n')#подпись оси X
# plt.ylabel('Частота резонанса, кГц')#подпись оси Y
# # plt.legend()#отображение названия прямой

plt.show()#воспроизведение всех графиков на экран

