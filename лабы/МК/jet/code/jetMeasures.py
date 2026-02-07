import jetFunctions as jet
import time
import numpy as np

try:
    steps = 0
    jet.initSpiAdc()
    jet.initStepMotorGpio()

    while True:
        n = input('Enter steps or command (h - help) > ')

        if n == 'h':
            print('\nHelp for "Jet Mover":')
            print('     50 - positive integer to step forward')
            print('    -80 - negative integer to step backward')
            print('      s - actual position relative to zero')
            print('      z - set zero')
            print('      q - exit')
            print('Try in now!\n')

        elif n == 's':
            print(steps, ' steps')

        elif n == 'z':
            steps = 0
            print(steps, ' steps')
        
        elif n == 'c':
            press = []
            for i in range(500):
                press.append(jet.getAdc())
                time.sleep(0.05)
            np.savetxt('cali_dist2.txt', press, delimiter = ',', fmt = '%.4f', header = '', comments ='', encoding = 'utf-8')
        
        elif n == 'm':
            steps = 0
            press = []
            stepo = int((913*2.1)//5)
            print(stepo)
            jet.stepBackward(stepo)
            for i in range(140):
                sum = 0
                for j in range(10):
                    sum += jet.getAdc()
                    time.sleep(0.05)
                press.append(sum/10)
                jet.stepForward(stepo//70)
                time.sleep(0.05)
            jet.stepBackward(- stepo + 140*(stepo//70))
            np.savetxt('data_70_2.txt', press, delimiter = ',', fmt = '%.4f', header = '', comments ='', encoding = 'utf-8')

        elif n == 'q':
            print(steps, ' steps') 
            break

        else:
            n = int(n)
            if n < 0:
                jet.stepBackward(abs(n))
            if n > 0:
                jet.stepForward(n)

            steps += n

finally:
    jet.deinitStepMotorGpio()
