import numpy as np
import matplotlib.pyplot as plt
import os

# Параметры
A = 418.9829
x_min = -500
x_max = 500
num_points = 2000

script_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(script_dir, "results")

if not os.path.exists(results_dir):
    os.makedirs(results_dir)
    print(f"Создана папка: {results_dir}")
else:
    print(f"Папка уже существует: {results_dir}")
output_file = os.path.join(results_dir, "result.txt")

x = np.linspace(x_min, x_max, num_points)
y = A - x * np.sin(np.sqrt(np.abs(x)))
print(f" Расчет выполнен для {num_points} точек")

with open(output_file, "w", encoding="utf-8") as file:
    file.write(f"# Результаты расчета функции f(x) = A - x * sin(sqrt(|x|))\n")
    file.write(f"# A = {A}, x in [{x_min}; {x_max}], points = {num_points}\n")
    for xi, yi in zip(x, y):
        file.write(f"{xi:.6f}    {yi:.6f}\n")
print(f"Результаты сохранены в файл: {output_file}")

plt.figure(figsize=(12, 6))
plt.plot(x, y, linewidth=1, color='blue')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.xlim(x_min, x_max)
plt.show()