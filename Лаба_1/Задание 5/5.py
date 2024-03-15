import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из файла
data = np.loadtxt(r"D:\3 курс\Теория электрической связи\Лаба 1 ЭС\Задание 5\Файлы_6\DATA3.txt")
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

# Рассчитываем данные для обобщенной функции Релея
A = np.linspace(0, max_x * 9, 1000)  # Создаем значения A для графика
sigma_squared = ((4-np.pi)/2)*max_x**2
A0 = 0.2
p_A = (A / sigma_squared) * np.exp(-(A**2 + A0**2) / (2 * sigma_squared)) * (1 + (A0**2 * A**2) / (4 * sigma_squared**2))

# График обобщенной функции Релея
plt.plot(A, p_A, 'r--', label='Обобщенная функция Райса', color = 'purple', linewidth = 0.8)
plt.grid(True)
plt.legend()
plt.show()

print("\nДисперсия замираний:", sigma_squared)
print("Детерминированная составляющая А0:", A0)
