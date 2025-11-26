import numpy as np
import matplotlib.pyplot as plt

def mnk(x, y):
    k=(sum(x*y)-sum(x)*sum(y)/len(y))/(sum(x**2)-sum(x)**2/len(y))
    b=(sum(y)-k*sum(x))/len(y)
    # sigma_k = (1/(len(x))**0.5)*((sum(y*y)-sum(y)*sum(y)/len(y))/(sum(x*x)-sum(x)*sum(x)/len(y))-k*k)**0.5
    # sigma_b = sigma_k*(sum(x*x)-sum(x)*sum(x)/len(x))**0.5
    # print("k: ", k, sigma_k, "b: ", b, sigma_b)
    return k, b 

data = np.loadtxt('C:/Users/User/Documents/engineering/new-repo/small_waves/exp/exp74.txt', delimiter = ',', encoding = 'utf-8')
time1 = data[-1]
time2 = data[-2]
time = time1-time2
x = []

data[-1] -= 12829*time//(len(data)-2)-0.4
time -= 12829*time//(len(data)-2)-0.4
data = data[12829:]

# for i in range(len(data)-2):
#     if i*time/(len(data)-2) > 6.8:
#         print(i)
#         break

for i in range(len(data)-2):
    x.append(i*time/(len(data)-2))
x = np.array(x)
np.savetxt('C:/Users/User/Documents/engineering/new-repo/small_waves/expo/expo74.txt', data, delimiter = ',', fmt = '%.4f', comments ='', encoding = 'utf-8')

# k1, b1 = mnk(x[0:int(1*(len(data)-2)/time)], data[0:int(1*(len(data)-2)/time)])
# k2, b2 = mnk(x[int(1.4*(len(data)-2)/time):int(2.5*(len(data)-2)/time)], data[int(1.4*(len(data)-2)/time):int(2.5*(len(data)-2)/time)])

plt.plot(x, data[0:-2])
# plt.plot(x[0:int(1.2*(len(data)-2)/time)], x[0:int(1.2*(len(data)-2)/)]*k1 + b1)
# plt.plot(x[int(1.2*(len(data)-2)/time):], x[int(1.2*(len(data)-2)/time):]time*k2 + b2, color = 'r')
plt.show()

# np.savetxt('expo20.txt', data, delimiter = ',', fmt = '%.4f', comments ='', encoding = 'utf-8')

# 100 - 1.33
# 74 - 1.54
# 60 - 1.7
# 40 - 2.1
# 20 - 3