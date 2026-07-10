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

def main():
    parser = argparse.ArgumentParser(description="Построение графика y=f(x) из текстового файла.")
    parser.add_argument("file", help="Путь к файлу с данными (2 столбца: x y)")
    parser.add_argument("--width", type=float, default=8.0, help="Ширина окна графика в дюймах (по умолчанию 8.0)")
    parser.add_argument("--height", type=float, default=6.0, help="Высота окна графика в дюймах (по умолчанию 6.0)")
    args = parser.parse_args()
    x_data, y_data = load_data(args.file)
    plot_graph(x_data, y_data, args)
if __name__ == "__main__":
    main()
