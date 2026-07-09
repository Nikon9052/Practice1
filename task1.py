import numpy as np
import matplotlib.pyplot as plt
import os

A = 418.9829
x_min = -500
x_max = 500
num_points = 2000  
output_dir = "results"
output_file = os.path.join(output_dir, "result.txt")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Директория '{output_dir}' создана.")
else:
    print(f"Директория '{output_dir}' уже существует.")