# spirograph_drawer_with_circles.py

import numpy as np
import matplotlib.pyplot as plt

def draw_spirograph(R, r, p, n_points=1000):
    # スピログラフの描画
    theta = np.linspace(0, 2 * np.pi * abs(R - r), n_points)
    x = (R - r) * np.cos(theta) + p * np.cos(((R - r) / r) * theta)
    y = (R - r) * np.sin(theta) - p * np.sin(((R - r) / r) * theta)

    plt.plot(x, y)

    # 外円の描画
    outer_circle_theta = np.linspace(0, 2 * np.pi, n_points)
    outer_circle_x = R * np.cos(outer_circle_theta)
    outer_circle_y = R * np.sin(outer_circle_theta)
    plt.plot(outer_circle_x, outer_circle_y, linestyle='dashed', color='gray')

    # 内円の描画
    inner_circle_theta = np.linspace(0, 2 * np.pi, n_points)
    inner_circle_x = (R - r) * np.cos(theta[-1]) + r * np.cos(inner_circle_theta)
    inner_circle_y = (R - r) * np.sin(theta[-1]) + r * np.sin(inner_circle_theta)
    plt.plot(inner_circle_x, inner_circle_y, linestyle='dashed', color='gray')

    # ペンの位置の描画
    pen_theta = np.arctan2(y[-1] - (R - r) * np.sin(theta[-1]), x[-1] - (R - r) * np.cos(theta[-1]))
    pen_x = (R - r) * np.cos(theta[-1]) + p * np.cos(pen_theta)
    pen_y = (R - r) * np.sin(theta[-1]) - p * np.sin(pen_theta)
    plt.plot([pen_x, (R - r) * np.cos(theta[-1])], [pen_y, (R - r) * np.sin(theta[-1])], color='red', linestyle='dotted')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f'Spirograph (R={R}, r={r}, p={p})')
    plt.show()

# 外円の半径 (R)、内円の半径 (r)、ペンの位置 (p) を設定します
R = 100
r = 75
p = 50

draw_spirograph(R, r, p)
