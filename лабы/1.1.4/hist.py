import pandas as pd
import numpy as np
from scipy import special
import matplotlib.pyplot as plt 

data = pd.read_csv('c:/Users/User/Documents/mipt_takonef/лабы/1.1.4/эксперимент/exp.csv', header=None)
data = data[0].to_numpy() # данные в нампай массив для удобства

# разбиваем на группы по tau элементов и суммируем их значения
group_sums_0 = data
group_sums_10 = np.sum(data.reshape(-1, 10), axis=1)
group_sums_20 = np.sum(data.reshape(-1, 20), axis=1)
group_sums_40 = np.sum(data.reshape(-1, 40), axis=1)
group_sums_80 = np.sum(data.reshape(-1, 80), axis=1)


# уникальные значения и их количество
unique_values, counts = np.unique(group_sums_80, return_counts=True)

mean_val = np.mean(group_sums_80) # среднее значение количества посчитанных частиц
std_val = np.sqrt(mean_val) # среднеквадратическая ошибка отдельного измерения

# диапазон значений для нормального распределения
x_range = np.linspace(min(unique_values)-3, max(unique_values)+2, 1000)
# значения нормального распределения
normal_dist = (1/(std_val * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_range - mean_val)/std_val)**2)

print(mean_val, std_val)
# plchldr = (2,718**(-mean_val))
puasson = ((mean_val**x_range)/(special.factorial(x_range)))/(2.718**(mean_val))

# кривая нормального распределения поверх гистограммы
# plt.plot(x_range, normal_dist, color='red', linewidth=2, 
#          label=f'Нормальное распределение\nμ={mean_val:.2f}, σ={std_val:.2f}')
# plt.legend()
plt.plot(x_range, puasson, color='blue', linewidth=2, label = "Распределение Пуассона")
plt.legend()

plt.bar(unique_values, counts/len(group_sums_80), 1,
        alpha=1,
        color = 'w', 
        edgecolor='black', 
        linewidth=0.7,)

plt.xlabel('Число отсчетов')
plt.ylabel('Доля случаев')
plt.grid(alpha=0.3, axis='y')  # сетка только по вертикали

plt.show()
# for i in range(len(unique_values)):
#     print(unique_values[i], end = ' & ')
# print(' \\\\')
# print('\\hline')

# for i in range(len(unique_values)):
#     print(counts[i], end = ' & ')  
# print(' \\\\')
# print('\\hline')  

# for i in range(len(unique_values)):
#     print(f'{counts[i]/len(group_sums_20):.3f}', end = ' & ')  
# print(' \\\\')
# print('\\hline') 

# for i in range(len(unique_values)):
#     print(f'{((mean_val**unique_values[i])/(special.factorial(unique_values[i])))/(2.718**(mean_val)):.3f}', end = ' & ')
# print(' \\\\')
# print('\\hline')

# for i in range(len(unique_values)):
#     print('|c', end = '')