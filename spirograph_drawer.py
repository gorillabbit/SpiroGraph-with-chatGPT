import numpy as np
import matplotlib.pyplot as plt

def draw_spirograph(R, r, p, n_points=1000):
    theta = np.linspace(0, 2 * np.pi * abs(R - r), n_points)
    x = (R - r) * np.cos(theta) + p * np.cos(((R - r) / r) * theta)
    y = (R - r) * np.sin(theta) - p * np.sin(((R - r) / r) * theta)

    plt.plot(x, y)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f'Spirograph (R={R}, r={r}, p={p})')
    plt.show()

# 外円の半径 (R)、内円の半径 (r)、ペンの位置 (p) を設定します
R = 100
r = 20
p = 0

draw_spirograph(R, r, p)
