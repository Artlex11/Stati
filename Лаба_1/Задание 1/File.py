import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("Файлы\\DATA3.txt", sep='\s\s', header=None)
data = pd.DataFrame(data)

X = data[0]
Y = data[1]

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Statistics')
plt.xlim(-6.5, 6.5)
plt.ylim(0, 0.3)
plt.plot(X, Y, label='Data')
plt.grid()
plt.legend(loc='upper left')
plt.show()
##print(data.head())

M_Y = max(data[1]) #максимум функции распределения 
print("Максимальное значение функции распределения: ", M_Y) #найти руками
M_Y_E = max(data[1])/np.e #максимум функции распредленеия делённое на е
print("M_Y_E", M_Y_E) 
D_Y = ((M_Y - M_Y_E)) ** 2 #максимум - максимум делённный на е , всё в квадрате 
print("D_Y", D_Y)
#M = data[0].mean()
#M_X = sum(X)/len(X)
#print(M)
###print(M_X)
#squared_deviations = [(x-M_X) ** 2 for x in X]
#D_X = sum(squared_deviations)/len(X)
#print(round(D_X, 5)) 