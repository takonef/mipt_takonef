import numpy as np

path = 'C:/Users/User/Documents/engineering/engi_takonef/jet/data/data_20_2.txt'
data = np.loadtxt(path, delimiter = ',', encoding = 'utf-8')

# for i in range(25): 
#         data[i] -= 100
for i in range(96, len(data)): 
        data[i] -= i
for i in range(86, len(data)): 
        data[i] -= i**1.2
data[96] += 200
np.savetxt('C:/Users/User/Documents/engineering/engi_takonef/jet/data/data_20_uh.txt', data, delimiter = ',', fmt = '%.4f', header = '', comments ='', encoding = 'utf-8')