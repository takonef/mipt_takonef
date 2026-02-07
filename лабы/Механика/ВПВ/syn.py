import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def read_data_from_file(filename):

    times = []
    values = []
    
    with open(filename, 'r', encoding='ANSI') as file:
        lines = file.readlines()
        
        # Пропускаем заголовок
        for line in lines[1:]:
            if line.strip():  # Пропускаем пустые строки
                # Заменяем запятые на точки для преобразования в float
                parts = line.strip().replace(',', '.').split()
                if len(parts) >= 2:
                    try:
                        t = float(parts[0])
                        wz = float(parts[1])
                        times.append(t)
                        values.append(wz)
                    except ValueError:
                        print(f"Ошибка преобразования данных в строке: {line}")
    
    return times, values

def peak_approx(bobs, bobs2, x, y, which, axs, i):
    if which:
        complete = [y[100:][bobs[0]]]
        x_complete = [x[100:][bobs[0]]]
    else:
        complete = [y[100:][bobs2[0]]]
        x_complete = [x[100:][bobs2[0]]]
    change = 0
    for j in range(1, min(len(bobs), len(bobs2))-2):
        if which:
            complete.append(y[100:][bobs[j]])
            x_complete.append(x[100:][bobs[j]])
            if (y[100:][bobs[j-1]]>=y[100:][bobs[j]] and y[100:][bobs[j+1]]>=y[100:][bobs[j]] and y[100:][bobs[j-1]]>y[100:][bobs[j+1]]):
                if change:
                    change -= 1
                    complete.pop()
                    x_complete.pop()
                    if change:
                        change -= 1
                        complete.pop()
                        x_complete.pop()
                else: 
                    which = 0
                    change = 4
            elif (y[100:][bobs[j]]>=y[100:][bobs[j+1]] and y[100:][bobs[j+2]]>=y[100:][bobs[j+1]] and y[100:][bobs[j]]<y[100:][bobs[j+2]]):
                if change:
                    change -= 1
                    complete.pop()
                    x_complete.pop()
                    if change:
                        change -= 1
                        complete.pop()
                        x_complete.pop()
                else: 
                    which = 0
                    change = 4
            if change:
                change -= 1
        else:
            complete.append(y[100:][bobs2[j]])
            x_complete.append(x[100:][bobs2[j]])
            if (y[100:][bobs2[j-1]]<=y[100:][bobs2[j]] and y[100:][bobs2[j+1]]<=y[100:][bobs2[j]] and y[100:][bobs2[j-1]]<y[100:][bobs2[j+1]]):
                if change:
                    change -= 1
                    complete.pop()
                    x_complete.pop()
                    if change:
                        change -= 1
                        complete.pop()
                        x_complete.pop()
                else: 
                    which = 1
                    change = 4
            elif (y[100:][bobs2[j]]<=y[100:][bobs2[j+1]] and y[100:][bobs2[j+2]]<=y[100:][bobs2[j+1]] and y[100:][bobs2[j]]>y[100:][bobs2[j+2]]):
                if change:
                    change -= 1
                    complete.pop()
                    x_complete.pop()
                    if change:
                        change -= 1
                        complete.pop()
                        x_complete.pop()
                else: 
                    which = 1
                    change = 4
            if change:
                change -= 1
    if which:
        for q in range(min(len(bobs), len(bobs2))-2, len(bobs)):

            complete.append(y[100:][bobs[q]])
            x_complete.append(x[100:][bobs[q]])
    else:
        for q in range(min(len(bobs), len(bobs2))-2, len(bobs2)):

            complete.append(y[100:][bobs2[q]])
            x_complete.append(x[100:][bobs2[q]])

    # axs[i].plot(x_complete, complete, 'xkcd:light royal blue', linestyle = '--', linewidth=2, label="Верхняя огибающая")

    coeffs = np.polyfit(x_complete, complete, 30)
    poly = np.poly1d(coeffs)
    axs[i].plot(x[2200:17400], poly(x[2200:17400]), 'xkcd:light royal blue', linestyle = '--', linewidth=2)
    
    timo = times(x[2200:17400], poly(x[2200:17400]), axs, i, 'blue')
    first = 1
    sum = 0
    count = 0
    for j in range(len(timo)):
        if timo[j] > 0:
            if first:
                first = 0
            else:
                sum += (timo[j] - timo[j-1])
                print(timo[j] - timo[j-1])
                count += 1

    print("T = ", sum/count)



def subplot_data(x, y, fig, axs, i):
    
    axs[i].plot(x[0:0], x[0:0], 'xkcd:light royal blue', linestyle = '--', linewidth=2, label="огибающая")
    axs[i].plot(x[2200:17400], y[2200:17400], label='зависимость W(t)', linestyle = '-',
            color = 'red', linewidth = 2,
            ms = 10) # ms - marker size, размер точек
    
    points = find_peaks(y[100:], height = 0.1) # max
    yy = -np.array(y)
    points2 = find_peaks(yy[100:], height = 0.1) # min
    
    bobs = []
    bobs.append(points[0][0])
    for j in range(1, len(points[0])):
        if x[points[0][j]] - x[points[0][j-1]] > 0.5:
            bobs.append(points[0][j])
            # axs[i].scatter(x[100:][points[0][j]], y[100:][points[0][j]])
    
    bobs2 = []
    bobs2.append(points2[0][0])
    for j in range(1, len(points2[0])):
        if x[points2[0][j]] - x[points2[0][j-1]] > 0.5:
            bobs2.append(points2[0][j])
            # axs[i].scatter(x[100:][points2[0][j]], y[100:][points2[0][j]])
    
    # peak_approx(bobs, bobs2, x, y, 0, axs, i)
    # peak_approx(bobs, bobs2, x, y, 1, axs, i)


    # timo = times(x[1000:-1000], y[1000:-1000], axs, i, 'blue')
    # first = 1
    # sum = 0
    # count = 0
    # for j in range(len(timo)):
    #     if timo[j] > 20 and timo[j] < 28:
    #         if first:
    #             first = 0
    #         else:
    #             sum += (timo[j] - timo[j-1])
    #             print(timo[j] - timo[j-1])
    #             count += 1
    #     if timo[j] > 28:
    #         break
    # print("T = ", sum/count)

    axs[i].set_xlabel('Время t, c') # + set!!!!!!
    axs[i].set_ylabel('Угловая скорость W, рад/c')
    axs[i].set_title('Маятник ' + str(i+1))

    axs[i].grid(which='major', linestyle = '-')
    axs[i].grid(which='minor', linestyle = '-.', linewidth = 0.2)
    axs[i].minorticks_on()

    axs[i].legend()

    fig.set_label('степени')     

def times(x, y, axs, i, colorr):
    timo = []
    for j in range(len(y)-1):
        if y[j] == 0:
            if y[j-1] == 0:
                pass
            else:
                axs[i].scatter(x[j], y[j], color = colorr)
                timo.append(x[j])
        elif y[j]*y[j+1] < 0:
            axs[i].scatter(x[j], (y[j]+y[j+1])/2, color = colorr)
            timo.append((x[j]+x[j+1])/2)
    return timo

def main():
    input_filename1 = "C:/Users/User/Documents/mipt_takonef/лабы/связанные_маятники/Б03-503/низ30/syn1.txt"  # Замените на имя вашего файла
    input_filename2 = "C:/Users/User/Documents/mipt_takonef/лабы/связанные_маятники/Б03-503/низ30/syn2.txt"  # Замените на имя вашего файла
    
    fig, axs = plt.subplots(nrows = 2, ncols = 1, figsize = (8, 8))
    try:

        times1, values1 = read_data_from_file(input_filename1)
        times2, values2 = read_data_from_file(input_filename2)

        # for i in range(len(times1)):
        #     if times1[i] == 10.9 or times1[i] == 95.5:
        #         print(i)

            
        subplot_data(times1, values1, fig, axs, 0)
        subplot_data(times2, values2, fig, axs, 1)

        plt.subplots_adjust(
            # left = 0.5,
            # right =1,
            # bottom =0.5,
            # top =1 
            # wspace =1 # горизонтальный отступ между графиками
            hspace = 0.5 # вертикальный отступ между графиками
        )
        axs[0].legend(loc = 'lower right')
        axs[1].legend(loc = 'lower right')
        plt.show()
        
    except FileNotFoundError:
        print(f"Файл не найден.")
        print("Пожалуйста, убедитесь, что файл существует в текущей директории.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()