import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.interpolate import CubicSpline

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

def find_local_extrema(x, y, find_min=False):
    """
    Находит локальные экстремумы в данных
    find_min=True: ищем минимумы
    find_min=False: ищем максимумы
    """
    if find_min:
        # Ищем локальные минимумы
        peaks, _ = find_peaks(-np.array(y), distance=5)  # инвертируем для поиска минимумов
    else:
        # Ищем локальные максимумы
        peaks, _ = find_peaks(y, distance=5)
    
    return peaks

def plot_envelope_with_extrema(ax, x_data, y_data, x_peaks, y_peaks, 
                               envelope_color='xkcd:light royal blue',
                               extrema_color='blue', 
                               envelope_label='Огибающая',
                               is_upper=True):
    """
    Рисует огибающую и отмечает экстремумы
    """
    if len(x_peaks) < 4:
        # Слишком мало точек для сплайна
        ax.plot(x_peaks, y_peaks, 'o-', color=envelope_color, 
                linestyle='--', linewidth=2, label=envelope_label)
    else:
        # Используем кубический сплайн
        cs = CubicSpline(x_peaks, y_peaks)
        
        # Создаем гладкую кривую для отображения
        x_smooth = np.linspace(min(x_peaks), max(x_peaks), 500)
        y_smooth = cs(x_smooth)
        
        # Рисуем огибающую
        ax.plot(x_smooth, y_smooth, color=envelope_color, 
                linestyle='--', linewidth=2, label=envelope_label)
    
    # Находим и отмечаем экстремумы на самой огибающей
    if len(y_peaks) > 10:  # Достаточно точек для поиска экстремумов
        if is_upper:
            # Для верхней огибающей ищем локальные минимумы
            minima_indices = find_local_extrema(x_peaks, y_peaks, find_min=True)
        else:
            # Для нижней огибающей ищем локальные максимумы
            maxima_indices = find_local_extrema(x_peaks, y_peaks, find_min=False)
        
        # Отмечаем точки на графике
        if is_upper and len(minima_indices) > 0:
            ax.scatter(np.array(x_peaks)[minima_indices], 
                      np.array(y_peaks)[minima_indices], 
                      color=extrema_color, s=50, zorder=5,
                      label='Минимумы верхней огибающей')
            print(f"Минимумы верхней огибающей (x, y):")
            for idx in minima_indices:
                print(f"  ({x_peaks[idx]:.2f}, {y_peaks[idx]:.4f})")
                
        elif not is_upper and len(maxima_indices) > 0:
            ax.scatter(np.array(x_peaks)[maxima_indices], 
                      np.array(y_peaks)[maxima_indices], 
                      color=extrema_color, s=50, zorder=5,
                      label='Максимумы нижней огибающей')
            print(f"Максимумы нижней огибающей (x, y):")
            for idx in maxima_indices:
                print(f"  ({x_peaks[idx]:.2f}, {y_peaks[idx]:.4f})")

def subplot_data(x, y, fig, axs, i):
    
    # Создаем фиктивный элемент для легенды
    axs[i].plot([], [], 'xkcd:light royal blue', linestyle='--', 
                linewidth=2, label="Огибающие")
    
    # Основные данные
    axs[i].plot(x[1500:11500], y[1500:11500], label='W(t)', 
                linestyle='-', color='red', linewidth=2)
    
    # Находим пики (максимумы и минимумы)
    points = find_peaks(y[1000:], height=0.1, distance=10)  # максимумы
    yy = -np.array(y)
    points2 = find_peaks(yy[1000:], height=0.1, distance=10)  # минимумы
    
    # Фильтруем максимумы (верхняя огибающая)
    bobs = []
    if len(points[0]) > 0:
        bobs.append(points[0][0])
        for j in range(1, len(points[0])):
            if x[1000:][points[0][j]] - x[1000:][points[0][j-1]] > 0.5:
                bobs.append(points[0][j])
    
    # Фильтруем минимумы (нижняя огибающая)
    bobs2 = []
    if len(points2[0]) > 0:
        bobs2.append(points2[0][0])
        for j in range(1, len(points2[0])):
            if x[1000:][points2[0][j]] - x[1000:][points2[0][j-1]] > 0.5:
                bobs2.append(points2[0][j])
    
    if i == 0:
        # Для первого графика используем вашу оригинальную функцию
        peak_approx(bobs, bobs2, x, y, 0, axs, i)
        peak_approx(bobs, bobs2, x, y, 1, axs, i)
    else: 
        # Подготовка данных для верхней огибающей (максимумы)
        x_up = []
        y_up = []
        for j in bobs:
            x_up.append(x[1000:][j])
            y_up.append(y[1000:][j])
            axs[i].scatter(x[1000:][j], y[1000:][j], color='purple', 
                          s=30, zorder=5, label='Максимумы W(t)')
        
        # Подготовка данных для нижней огибающей (минимумы)
        x_down = []
        y_down = []
        for j in bobs2:
            x_down.append(x[1000:][j])
            y_down.append(y[1000:][j])
            axs[i].scatter(x[1000:][j], y[1000:][j], color='orange', 
                          s=30, zorder=5, label='Минимумы W(t)')
        
        print(f"\n=== Маятник {i+1} ===")
        print(f"Найдено максимумов: {len(x_up)}, минимумов: {len(x_down)}")
        
        # Верхняя огибающая с отмеченными минимумами
        if len(x_up) > 3:
            plot_envelope_with_extrema(axs[i], x[1500:10500], y[1500:10500],
                                      x_up, y_up, 
                                      envelope_color='xkcd:light royal blue',
                                      extrema_color='blue',
                                      envelope_label='Верхняя огибающая',
                                      is_upper=True)
        
        # Нижняя огибающая с отмеченными максимумами
        if len(x_down) > 3:
            plot_envelope_with_extrema(axs[i], x[1500:10500], y[1500:10500],
                                      x_down, y_down,
                                      envelope_color='xkcd:green',
                                      extrema_color='green',
                                      envelope_label='Нижняя огибающая',
                                      is_upper=False)
    
    # Настройки графика
    axs[i].set_xlabel('Время t, c')
    axs[i].set_ylabel('Угловая скорость W, рад/c')
    axs[i].set_title(f'Маятник {i+1}')
    
    axs[i].grid(which='major', linestyle='-')
    axs[i].grid(which='minor', linestyle='-.', linewidth=0.2)
    axs[i].minorticks_on()
    
    # Ограничиваем легенду, чтобы избежать дублирования
    if i == 1:
        # Получаем текущие метки легенды
        handles, labels = axs[i].get_legend_handles_labels()
        # Удаляем дубликаты
        unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) 
                 if l not in labels[:i]]
        # Обновляем легенду
        axs[i].legend(*zip(*unique), loc='best')

    fig.set_label('степени')

def peak_approx(bobs, bobs2, x, y, which, axs, i):
    # Ваша оригинальная функция (сохранена без изменений)
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
            if (y[1000:][bobs[j-1]]>=y[1000:][bobs[j]] and 
                y[1000:][bobs[j+1]]>=y[1000:][bobs[j]] and 
                y[1000:][bobs[j-1]]>y[1000:][bobs[j+1]]):
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
            elif (y[1000:][bobs[j]]>=y[1000:][bobs[j+1]] and 
                  y[1000:][bobs[j+2]]>=y[1000:][bobs[j+1]] and 
                  y[1000:][bobs[j]]<y[1000:][bobs[j+2]]):
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
            if (y[1000:][bobs2[j-1]]<=y[1000:][bobs2[j]] and 
                y[1000:][bobs2[j+1]]<=y[1000:][bobs2[j]] and 
                y[1000:][bobs2[j-1]]<y[1000:][bobs2[j+1]]):
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
            elif (y[1000:][bobs2[j]]<=y[1000:][bobs2[j+1]] and 
                  y[1000:][bobs2[j+2]]<=y[1000:][bobs2[j+1]] and 
                  y[1000:][bobs2[j]]>y[1000:][bobs2[j+2]]):
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

    # Полиномиальная аппроксимация
    if len(x_complete) > 30:  # Достаточно точек для полинома 30-й степени
        coeffs = np.polyfit(x_complete, complete, min(30, len(x_complete)-1))
        poly = np.poly1d(coeffs)
        axs[i].plot(x[1500:11500], poly(x[1500:11500]), 
                   'xkcd:light royal blue', linestyle='--', linewidth=2)
        
        # Находим и отмечаем экстремумы полинома
        if which:  # Верхняя огибающая - ищем минимумы
            # Производная полинома
            poly_deriv = np.polyder(poly)
            # Корни производной (экстремумы)
            roots = np.roots(poly_deriv)
            # Фильтруем действительные корни в диапазоне данных
            real_roots = roots[np.isreal(roots)].real
            valid_roots = [r for r in real_roots 
                          if min(x_complete) <= r <= max(x_complete)]
            
            # Вычисляем вторую производную для определения минимумов
            poly_deriv2 = np.polyder(poly_deriv)
            for root in valid_roots:
                if poly_deriv2(root) > 0:  # Вторая производная > 0 => минимум
                    axs[i].scatter(root, poly(root), color='blue', 
                                  s=100, marker='*', zorder=6,
                                  label='Минимум верхней огибающей')

def main():
    input_filename1 = "C:/Users/User/Documents/mipt_takonef/лабы/связанные_маятники/Б03-503/рассинхрон_423_34/1beat1.txt"
    input_filename2 = "C:/Users/User/Documents/mipt_takonef/лабы/связанные_маятники/Б03-503/рассинхрон_423_34/1beat2.txt"
    
    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))
    
    try:
        times1, values1 = read_data_from_file(input_filename1)
        times2, values2 = read_data_from_file(input_filename2)
        
        subplot_data(times1, values1, fig, axs, 0)
        subplot_data(times2, values2, fig, axs, 1)
        
        plt.subplots_adjust(hspace=0.5)
        
        # Настройка легенды для первого графика
        if axs[0].get_legend() is None:
            axs[0].legend(loc='best')
        
        plt.show()
        
    except FileNotFoundError:
        print(f"Файл не найден.")
        print("Пожалуйста, убедитесь, что файл существует в текущей директории.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()