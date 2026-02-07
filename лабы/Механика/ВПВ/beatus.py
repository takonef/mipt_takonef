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
        complete = [y[1000:][bobs[0]]]
        x_complete = [x[1000:][bobs[0]]]
    else:
        complete = [y[1000:][bobs2[0]]]
        x_complete = [x[1000:][bobs2[0]]]
    change = 0
    for j in range(1, min(len(bobs), len(bobs2))-2):
        if which:
            complete.append(y[1000:][bobs[j]])
            x_complete.append(x[1000:][bobs[j]])
            if (y[1000:][bobs[j-1]]>=y[1000:][bobs[j]] and y[1000:][bobs[j+1]]>=y[1000:][bobs[j]] and y[1000:][bobs[j-1]]>y[1000:][bobs[j+1]]):
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
            elif (y[1000:][bobs[j]]>=y[1000:][bobs[j+1]] and y[1000:][bobs[j+2]]>=y[1000:][bobs[j+1]] and y[1000:][bobs[j]]<y[1000:][bobs[j+2]]):
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
            complete.append(y[1000:][bobs2[j]])
            x_complete.append(x[1000:][bobs2[j]])
            if (y[1000:][bobs2[j-1]]<=y[1000:][bobs2[j]] and y[1000:][bobs2[j+1]]<=y[1000:][bobs2[j]] and y[1000:][bobs2[j-1]]<y[1000:][bobs2[j+1]]):
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
            elif (y[1000:][bobs2[j]]<=y[1000:][bobs2[j+1]] and y[1000:][bobs2[j+2]]<=y[1000:][bobs2[j+1]] and y[1000:][bobs2[j]]>y[1000:][bobs2[j+2]]):
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

            complete.append(y[1000:][bobs[q]])
            x_complete.append(x[1000:][bobs[q]])
    else:
        for q in range(min(len(bobs), len(bobs2))-2, len(bobs2)):

            complete.append(y[1000:][bobs2[q]])
            x_complete.append(x[1000:][bobs2[q]])

    # axs[i].plot(x_complete, complete, 'xkcd:light royal blue', linestyle = '--', linewidth=2, label="Верхняя огибающая")

    coeffs = np.polyfit(x_complete, complete, 30)
    poly = np.poly1d(coeffs)
    axs[i].plot(x[1500:11500], poly(x[1500:11500]), 'xkcd:light royal blue', linestyle = '--', linewidth=2)
    
    timo = times(x[1500:11500], poly(x[1500:11500]), axs, i, 'blue')
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
    
    axs[i].plot(x[1500:11500], y[1500:11500], label='зависимость W(t)', linestyle = '-',
            color = 'red', linewidth = 2,
            ms = 10) # ms - marker size, размер точек
    
    points = find_peaks(y[1000:], height = 0.1) # max
    yy = -np.array(y)
    points2 = find_peaks(yy[1000:], height = 0.1) # min
    
    bobs = []
    bobs.append(points[0][0])
    for j in range(1, len(points[0])):
        if x[points[0][j]] - x[points[0][j-1]] > 0.5:
            bobs.append(points[0][j])
            # axs[i].scatter(x[1000:][points[0][j]], y[1000:][points[0][j]])
    
    bobs2 = []
    bobs2.append(points2[0][0])
    for j in range(1, len(points2[0])):
        if x[points2[0][j]] - x[points2[0][j-1]] > 0.5:
            bobs2.append(points2[0][j])
            # axs[i].scatter(x[1000:][points2[0][j]], y[1000:][points2[0][j]])
    
    if i == 0:
        peak_approx(bobs, bobs2, x, y, 0, axs, i)
        peak_approx(bobs, bobs2, x, y, 1, axs, i)

    else: 
        x_up = []
        y_up = []
        for j in bobs:
            x_up.append(x[1000:][j])
            y_up.append(y[1000:][j])

        x_down = []
        y_down = []
        for j in bobs2:
            x_down.append(x[1000:][j])
            y_down.append(y[1000:][j])

        from scipy.interpolate import CubicSpline
        
        # Для верхней огибающей
        if len(x_up) > 3:
            cs_up = CubicSpline(x_up, y_up)
            x_smooth = np.linspace(x[1500:11500][0], x[1500:11500][9999], 500)
            axs[i].plot(x_smooth, cs_up(x_smooth), 
                       'xkcd:light royal blue', 
                       linestyle='--', 
                       linewidth=2,
                       label='огибающие')
        
        # Для нижней огибающей
        if len(x_down) > 3:
            cs_down = CubicSpline(x_down, y_down)
            x_smooth_down = np.linspace(x[1500:11500][0], x[1500:11500][9999], 500)
            axs[i].plot(x_smooth_down, cs_down(x_smooth_down), 
                       'xkcd:light royal blue', 
                       linestyle='--', 
                       linewidth=2) 
        pointis = find_peaks(cs_up(x_smooth), height = 0.4) # max
        pointis2 = find_peaks(-np.array(cs_down(x_smooth_down)), height = 0.4) # min
        
        bobis = []
        bobis.append(pointis[0][0])
        for j in range(len(pointis[0])):
            axs[1].scatter(x_smooth[pointis[0][j]], cs_up(x_smooth)[pointis[0][j]], color = 'xkcd:light royal blue')

        for j in range(len(pointis2[0])):
            axs[1].scatter(x_smooth_down[pointis2[0][j]], cs_down(x_smooth_down)[pointis2[0][j]], color = 'xkcd:light royal blue')

        min = 100
        ind = 0
        for j in range(len(cs_up(x_smooth))):
            if cs_up(x_smooth)[j] < min:
                min = cs_up(x_smooth)[j]
                ind = j
        
        axs[1].scatter(x_smooth[ind], min, color = 'xkcd:light royal blue')
        print("min: ", min)


        print("T2 = ", (x_smooth[pointis[0][len(pointis[0])-1]] - x_smooth[pointis[0][0]])/(len(pointis[0])-1))
        A0 = cs_up(x_smooth)[pointis[0][0]]
        An = cs_up(x_smooth)[pointis[0][len(pointis[0])-1]]
        print(0, A0)
        print(len(pointis[0])-1,  An)
        print(A0/An)    
        
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
    
    # for i in range(len(times1)):
    #     if times1[i] == 10.9 or times1[i] == 95.5:
    #         print(i)


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

# # низ 30:
# 0.6400000000000006
# 0.6275000000000013
# 0.625
# 0.6174999999999997
# 0.6225000000000023
# 0.6224999999999987
# 0.6199999999999974
# 0.6224999999999987
# 0.6275000000000013
# 0.625
# 0.6400000000000006
# T =  0.6263636363636365

# 8.360000000000003
# 8.36
# 8.329999999999998
# 8.344999999999999
# 8.310000000000002
# 8.33999999999999
# 8.350000000000009
# 8.295000000000002
# T =  8.33625

# рассинхрон 42.3 34
# 6.254999999999999
# 6.359999999999999
# 6.32
# 6.265000000000001
# 6.310000000000002
# 6.25
# T1 =  6.293333333333334
# T2 =  6.295295591182364
# A0 0.7992707846137863
# A6 0.6445566600257104
# A6 min:  0.31483191509726177
# 1.2400318454267536 - декр??
# T1 =  0.5394642857142856
# T2 =  0.5438461538461539

def main():
    input_filename1 = "C:/Users/User/Documents/mipt_takonef/лабы/связанные_маятники/Б03-503/рассинхрон_423_34/1beat1.txt"  # Замените на имя вашего файла
    input_filename2 = "C:/Users/User/Documents/mipt_takonef/лабы/связанные_маятники/Б03-503/рассинхрон_423_34/1beat2.txt"  # Замените на имя вашего файла
    
    fig, axs = plt.subplots(nrows = 2, ncols = 1, figsize = (8, 8))

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
    axs[0].plot([], [], 'xkcd:light royal blue', linestyle = '--', linewidth=2, label="огибающая")

    axs[0].legend(loc = 'lower right')
    axs[1].legend(loc = 'lower right')
    plt.show()


if __name__ == "__main__":
    main()