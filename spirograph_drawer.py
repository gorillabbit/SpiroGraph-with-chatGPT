import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def draw_spirograph(R, r, p, n_points=1000):
    theta = np.linspace(0, 2 * np.pi * abs((r * 1.0) / np.gcd(R, r)), n_points)
    x = (R - r) * np.cos(theta) + p * np.cos(((R - r) / r) * theta)
    y = (R - r) * np.sin(theta) - p * np.sin(((R - r) / r) * theta)
    return x, y

def update(frame, R, r, p, x, y):
    plt.gca().clear()

    # 外円の描画
    outer_circle_theta = np.linspace(0, 2 * np.pi, 1000)
    outer_circle_x = R * np.cos(outer_circle_theta)
    outer_circle_y = R * np.sin(outer_circle_theta)
    plt.plot(outer_circle_x, outer_circle_y, linestyle='dashed', color='gray')

    # 内円の描画
    inner_circle_theta = np.linspace(0, 2 * np.pi, 1000)
    inner_circle_x = (R - r) * np.cos(theta[frame]) + r * np.cos(inner_circle_theta)
    inner_circle_y = (R - r) * np.sin(theta[frame]) + r * np.sin(inner_circle_theta)
    plt.plot(inner_circle_x, inner_circle_y, linestyle='dashed', color='gray')

    # ペン先と内円の中心を結んだ線分
    pen_x = (R - r) * np.cos(theta[frame]) + p * np.cos(((R - r) / r) * theta[frame])
    pen_y = (R - r) * np.sin(theta[frame]) - p * np.sin(((R - r) / r) * theta[frame])
    plt.plot([pen_x, (R - r) * np.cos(theta[frame])], [pen_y, (R - r) * np.sin(theta[frame])], color='blue', linestyle='dotted')

    # スピログラフの描画
    plt.plot(x[:frame], y[:frame])

    # ペンの位置の描画
    plt.plot(pen_x, pen_y, 'ro')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f'Spirograph (R={R}, r={r}, p={p})')

R = 100
r = 75
p = 50
n_points = 1000
speed = 0.1  # アニメーションのフレーム更新間隔（ミリ秒）

x, y = draw_spirograph(R, r, p, n_points)
theta = np.linspace(0, 2 * np.pi * abs((r * 1.0) / np.gcd(R, r)), n_points)

fig = plt.figure()
ani = FuncAnimation(fig, update, frames=range(n_points), fargs=(R, r, p, x, y), interval=speed, repeat=True)
plt.show()

