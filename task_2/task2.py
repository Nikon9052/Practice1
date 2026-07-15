import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2): 
    return 0.5 + (np.sin(x1**2 - x2**2)**2 - 0.5) / (1 + 0.001 * (x1**2 + x2**2))**2

x1_range = [-2.0, 2.0]
x2_range = [-2.0, 2.0]
test_point = (0.0, 0.0)  # (x10, x20)

N = 100  
x10, x20 = test_point
f_test = f(x10, x20)

x1 = np.linspace(x1_range[0], x1_range[1], N)
x2 = np.linspace(x2_range[0], x2_range[1], N)
X1, X2 = np.meshgrid(x1, x2)
Z = f(X1, X2)

fig = plt.figure(figsize=(16, 12))
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
surf = ax1.plot_surface(X1, X2, Z, cmap='viridis', edgecolor='none')
ax1.set_title('3D Поверхность (Изометрия)')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y=f(x1, x2)')
ax1.scatter(x10, x20, f_test, color='red', s=50, label='Тестовая точка')
ax1.legend()

ax2 = fig.add_subplot(2, 2, 2)
contour = ax2.contourf(X1, X2, Z, levels=50, cmap='viridis')
ax2.set_title('Вид сверху')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
fig.colorbar(contour, ax=ax2, label='y=f(x1, x2)')
ax2.plot(x10, x20, 'ro', markersize=8, label='Точка (0,0)')
plt.grid(True, linestyle='--', alpha=0.7)
ax2.legend()

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(x1, f(x1, x20), 'b-', linewidth=2)
ax3.set_title(f'График y = f(x1) при x2 = {x20}')
ax3.set_xlabel('x1')
ax3.set_ylabel('y=f(x1, x2)')
ax3.grid(True)
ax3.plot(x10, f_test, 'ro', markersize=8)

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(x2, f(x10, x2), 'g-', linewidth=2)
ax4.set_title(f'График y = f(x2) при x1 = {x10}')
ax4.set_xlabel('x2')
ax4.set_ylabel('y=f(x1, x2)')
ax4.grid(True)
ax4.plot(x20, f_test, 'ro', markersize=8)

info_text = (
    f"Тестовая точка:\n"
    f"x1 = {x10}\n"
    f"x2 = {x20}\n"
    f"f(x1, x2) = {f_test:.6f}"
)
fig.text(0.02, 0.98, info_text, fontsize=12, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()