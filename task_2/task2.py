import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2): return 0.5 + ((x1**2 - x2**2)**2 - 0.5) / (1 + 0.001 * (x1**2 + x2**2))**2

x1_range = [-2.0, 2.0]
x2_range = [-2.0, 2.0]
test_point = (0.0, 0.0)  # (x10, x20)

N = 100  
x10, x20 = test_point
f_test = f(x10, x20)