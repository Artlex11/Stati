import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(r"D:\3 курс\Теория электрической связи\Лаба 1 ЭС\Задание 1\Файлы\DATA3.txt")
x_data = data[:, 0]
y_data = data[:, 1]

# Максимум функции плотности вероятности
max_y = np.max(y_data)
max_x_index = np.argmax(y_data)
max_x = x_data[max_x_index]
print("Максимум функции плотности вероятности: ", max_y)
print("Значение X, при котором функция плотности вероятности принимает максимум: ", max_x)

# График функции плотности вероятности
plt.plot(x_data, y_data, label='Функция плотности вероятности')
plt.xlabel('')
plt.ylabel('')
plt.title('Функция плотности вероятности')

# Вычисление параметров нормального распределения
mean = max_x
variance = 1 / (max_y ** 2 * 2 * np.pi)

# Генерация значений для нормального распределения
x_normal = np.linspace(np.min(x_data), np.max(x_data), 1000)
y_normal = 1 / np.sqrt(2 * np.pi * variance) * np.exp(-(x_normal - mean)**2 / (2 * variance))
# График нормального распределения
plt.plot(x_normal, y_normal, '--')
plt.grid(True)
plt.show()

print("\nСреднее значение:", mean)
print("Дисперсия:", variance)
