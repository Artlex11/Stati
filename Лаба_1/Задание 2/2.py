import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из файла
data = np.loadtxt(r"D:\3 курс\Теория электрической связи\Лаба 1 ЭС\Лаба1\2\DATA3.txt")
x_data = data[:, 0]
y_data = data[:, 1]

# Максимум функции плотности вероятности
max_y = np.max(y_data)
max_x_index = np.argmax(y_data)
max_x = x_data[max_x_index]
print("Максимум функции плотности вероятности: ", max_y)
print("Значение X, при котором функция плотности вероятности принимает максимум: ", max_x)

# График функции плотности вероятности
plt.plot(x_data, y_data, label='Функция плотности вероятности', color = 'orange', linewidth = 0.8)
plt.xlabel('')
plt.ylabel('')
plt.title('Функция плотности вероятности')
# Рассчитываем данные для распределения Релея
releev_x = np.linspace(0, max_x * 9, 1000)  # Создаем значения x для графика
releev_y = releev_x / (max_x ** 2) * np.exp(-releev_x ** 2 / (2 * max_x ** 2))
# График распределения Релея
plt.plot(releev_x, releev_y, 'r--', label='Релеевское распределение', color = 'purple', linewidth = 0.8)
plt.grid(True)
plt.legend()
plt.show()

print("\nРелеевский параметр:", max_x)
average = np.sqrt(np.pi / 2) * max_x
print("Среднее значение амплитуды:", average)
dispersia = ((4 - np.pi) / 2) * max_x ** 2
print("Дисперсия амплитуды:", dispersia)
sko = np.sqrt(dispersia)
print("СКО амплитуды:", sko)
median = 1.1774 * max_x
print("Медианное значение амплитуды:", median)
power = 2 * max_x ** 2
print("Средняя мощность амплитуды:", power)
F = 1 - np.exp(-((10 ** (-0.5) * median) ** 2) / (2 * max_x ** 2))
# Преобразование вероятности F в проценты
F_percent = F * 100
print("Вероятность, того что амплитуда сигнала будет принимать значения, меньше медианного на 10дБ:", round(F_percent, 2), "%")
