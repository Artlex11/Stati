import matplotlib.pyplot as plt
import numpy as np

# Чтение данных из файла
file_path = r"D:\3 курс\Теория электрической связи\Лаба 1 ЭС\Задание 4\Файлы_6\DATA3.txt"
x_cos = []
y_cos = []
x_sin = []
y_sin = []
with open(file_path, 'r') as file:
    lines = file.readlines()
    # Ищем разделитель между двумя функциями
    separator_index = lines.index('\n')
    # Чтение данных первой функции
    for line in lines[:separator_index]:
        x, y = map(float, line.split())
        x_cos.append(x)
        y_cos.append(y)
    # Чтение данных второй функции
    for line in lines[separator_index + 1:]:
        x, y = map(float, line.split())
        x_sin.append(x)
        y_sin.append(y)

# Находим максимумы и соответствующие значения X
max_y_cos = max(y_cos)
max_y_sin = max(y_sin)
x_max_cos = x_cos[y_cos.index(max_y_cos)]
x_max_sin = x_sin[y_sin.index(max_y_sin)]
print("Максимальное значение функции cos:", max_y_cos, "при x =", x_max_cos)
print("Максимальное значение функции sin:", max_y_sin, "при x =", x_max_sin)


print("\nСреднее значение для косинусной квадратуры:", x_max_cos)
print("Среднее значение для синусной квадратуры:", x_max_sin)
dis_cos = 1 / (max_y_cos ** 2 * 2 * np.pi)
print("Дисперсия для косинусной квадратуры:", dis_cos)
# sko_cos = np.sqrt(dis_cos)
# print(sko_cos)
dis_sin = 1 / (max_y_sin ** 2 * 2 * np.pi)
print("Дисперсия для синусной квадратуры:", dis_sin)
# sko_sin = np.sqrt(dis_sin)
# print(sko_sin)

# Построение графиков
plt.plot(x_cos, y_cos, label='cos', linewidth = 0.8)
plt.plot(x_sin, y_sin, label='sin', linewidth = 0.8)

# Добавляем нормальное распределение
x_values_cos = np.linspace(min(x_cos), max(x_cos), 100)
y_values_cos = np.exp(-(x_values_cos - x_max_cos)**2 / (2 * dis_cos)) / np.sqrt(2 * np.pi * dis_cos)
plt.plot(x_values_cos, y_values_cos, linestyle='--', color='green', linewidth = 0.8)

x_values_sin = np.linspace(min(x_sin), max(x_sin), 100)
y_values_sin = np.exp(-(x_values_sin - x_max_sin)**2 / (2 * dis_sin)) / np.sqrt(2 * np.pi * dis_sin)
plt.plot(x_values_sin, y_values_sin, linestyle='--', color='red', linewidth = 0.8)

plt.title("Функции плотности вероятности")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()
