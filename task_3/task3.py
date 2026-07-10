import argparse
import numpy as np
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    try:
        data = np.loadtxt(file_path, comments='#')
        
        if data.ndim == 1 or data.shape[1] < 2:
            raise ValueError("Файл должен содержать минимум два столбца данных (x и y).")
            
        x_data = data[:, 0]
        y_data = data[:, 1]
        
        return x_data, y_data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        exit(1)

def plot_graph(x_data, y_data, args):
    fig, ax = plt.subplots(figsize=(args.width, args.height))
    ax.plot(x_data, y_data, label="f(x) = A - x*sin(sqrt(|x|))")
    ax.set_title("График функции из Задания 1")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()