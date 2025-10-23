from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def mnk(x, y):
    k=(sum(x*y)-sum(x)*sum(y)/len(y))/(sum(x**2)-sum(x)**2/len(y))
    b=(sum(y)-k*sum(x))/len(y)
    print(k,b)
    return [k, b]

bestBubble = np.array(pd.read_csv('C:/Users/User/Documents/cpp/bestBubble.csv', header = None, sep = ', '))[0]
worstBubble = np.array(pd.read_csv('C:/Users/User/Documents/cpp/worstBubble.csv', header = None, sep = ', '))[0]

bestQuick = np.array(pd.read_csv('C:/Users/User/Documents/cpp/bestInsertion.csv', header = None, sep = ', '))[0]
worstQuick = np.array(pd.read_csv('C:/Users/User/Documents/cpp/worstQuick.csv', header = None, sep = ', '))[0]

bestInsertion = np.array(pd.read_csv('C:/Users/User/Documents/cpp/bestInsertion.csv', header = None, sep = ', '))[0]
worstInsertion = np.array(pd.read_csv('C:/Users/User/Documents/cpp/worstInsertion.csv', header = None, sep = ', '))[0]

bubble = np.array(pd.read_csv('C:/Users/User/Documents/cpp/bubbleSort2.csv', header = None, sep = ', '))[0]
shaker = np.array(pd.read_csv('C:/Users/User/Documents/cpp/shakerSort2.csv', header = None, sep = ', '))[0]
insertion = np.array(pd.read_csv('C:/Users/User/Documents/cpp/insertionSort2.csv', header = None, sep = ', '))[0]
python_insertion = np.array([0.0373992919921875, 0.06449332237243652, 0.1158332347869873, 0.1837836265563965, 0.2662493228912354, 0.3684370517730713, 0.46317253112792967, 0.5789521217346192, 0.7265143394470215, 0.8908751010894775, 1.0407089233398437, 1.2194367885589599, 1.461616849899292, 3.256653356552124, 3.642689609527588, 2.110644054412842, 2.404659557342529, 2.6413911819458007, 2.964616632461548, 3.306232976913452, 3.6278286933898927, 4.0332558155059814, 4.372459650039673, 4.705459547042847, 5.847331523895264, 5.800360155105591, 6.279256772994995, 7.696094751358032, 9.564432144165039, 9.069935417175293, 9.535541677474976, 10.168565225601196, 11.414271831512451, 12.567637729644776, 12.313840389251709, 12.949815130233764, 13.82299451828003, 13.321677255630494, 14.313700723648072])

heap = np.array(pd.read_csv('C:/Users/User/Documents/cpp/heapSort2.csv', header = None, sep = ', '))[0]
merge = np.array(pd.read_csv('C:/Users/User/Documents/cpp/mergeSort2.csv', header = None, sep = ', '))[0]
quick = np.array(pd.read_csv('C:/Users/User/Documents/cpp/quickSort2.csv', header = None, sep = ', '))[0]

# print(bubble, shaker, insertion)
# print(heap, merge, quick)

x = np.array([0]*len(bubble))
for i in range(len(bubble)):
    x[i] = 500*i + 1000

plt.plot(x, worstInsertion, label='C++')
plt.plot(x, python_insertion, label='Python')

plt.legend()
plt.grid(which='major', linestyle = '-')
plt.ylabel('sorting time, sec')
plt.xlabel('elements in an array')
plt.show()

x_log = np.log(x)
bubble_log = np.log(bubble)
shaker_log = np.log(shaker)
insertion_log = np.log(insertion)

# plt.plot(x, worstInsertion, label='worst case', color = 'purple')
# plt.plot(x, quick, label='random')
# plt.plot(x, bestInsertion, label='best case')

# plt.legend()
# plt.grid(which='major', linestyle = '-')
# plt.ylabel('sorting time, sec')
# plt.xlabel('elements in an array')
# plt.show()


# plt.plot(x, bubble, label='bubble sort')
# plt.plot(x, shaker, label='shaker sort')
# plt.plot(x, insertion, label='insertion sort')

# plt.legend()
# plt.grid(which='major', linestyle = '-')
# plt.ylabel('sorting time, sec')
# plt.xlabel('elements in an array')
# plt.show()


# plt.plot(x, heap, label='heap sort')
# plt.plot(x, merge, label='merge sort')
# plt.plot(x, quick, label='quick sort')

# plt.legend()
# plt.grid(which='major', linestyle = '-')
# plt.ylabel('sorting time, sec')
# plt.xlabel('elements in an array')
# plt.show()


# plt.plot(x, bubble, label='bubble sort')
# plt.plot(x, shaker, label='shaker sort')
# plt.plot(x, insertion, label='insertion sort')
# plt.plot(x, heap, label='heap sort')
# plt.plot(x, merge, label='merge sort')
# plt.plot(x, quick, label='quick sort')

# plt.legend()
# plt.grid(which='major', linestyle = '-')
# plt.ylabel('sorting time, sec')
# plt.xlabel('elements in an array')
# plt.show()

# plt.plot(x_log, mnk(x_log, bubble_log)[0]*x_log + mnk(x_log, bubble_log)[1], linewidth = 1, label = f'bubble sort; k = {mnk(x_log, bubble_log)[0]:.3f}, b = {mnk(x_log, bubble_log)[1]:.3f}')
# plt.plot(x_log, mnk(x_log, shaker_log)[0]*x_log + mnk(x_log, shaker_log)[1], linewidth = 1, label = f'shaker sort; k = {mnk(x_log, shaker_log)[0]:.3f}, b = {mnk(x_log, shaker_log)[1]:.3f}')
# plt.plot(x_log, mnk(x_log, insertion_log)[0]*x_log + mnk(x_log, insertion_log)[1], linewidth = 1, label = f'bubble sort; k = {mnk(x_log, insertion_log)[0]:.3f}, b = {mnk(x_log, insertion_log)[1]:.3f}')

# plt.scatter(x_log, bubble_log, s = 2.5)
# plt.scatter(x_log, shaker_log, s = 2.5)
# plt.scatter(x_log, insertion_log, s = 2.5)

# plt.legend()
# plt.grid(which='major', linestyle = '-')
# plt.ylabel('sorting time, sec')
# plt.xlabel('elements in an array')
# plt.show()

# heap = ((heap/x_log)/x)[4:]
# merge = ((merge/x_log)/x)[4:]
# quick = ((quick/x_log)/x)[4:]
# x = x[4:]

# plt.plot(x, mnk(x, heap)[0]*x + mnk(x, heap)[1], linewidth = 1, label = f'heap sort; k = -2,72e-15, b = 7.24e-09')
# plt.plot(x, mnk(x, merge)[0]*x + mnk(x, merge)[1], linewidth = 1, label = f'merge sort; k = -1.71e-15, b = 6.44e-09')
# plt.plot(x, mnk(x, quick)[0]*x + mnk(x, quick)[1], linewidth = 1, label = f'quick sort; k = -1.27e-14, b = 5.32e-09')

# plt.scatter(x, heap, s = 2.5)
# plt.scatter(x, merge, s = 2.5)
# plt.scatter(x, quick, s = 2.5)

# plt.legend()
# plt.grid(which='major', linestyle = '-')
# plt.ylabel('sorting time/NlogN')
# plt.xlabel('elements in an array')
# plt.show()