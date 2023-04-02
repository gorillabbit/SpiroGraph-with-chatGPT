import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def spirograph_theta(R, r, n_points):
    return np.linspace(0, 2 * np.pi * abs((r * 1.0) / np.gcd(R, r)), n_points)

def spirograph_xy(R, r, p, theta):
    x = (R - r) * np.cos(theta) + p * np.cos(((R - r) / r) * theta)
    y = (R - r) * np.sin(theta) - p * np.sin(((R - r) / r) * theta)
    return x, y

def plot_circle(radius, theta, x_offset=0, y_offset=0, linestyle='dashed', color='gray'):
    x = x_offset + radius * np.cos(theta)
    y = y_offset + radius * np.sin(theta)
    plt.plot(x, y, linestyle=linestyle, color=color)

def plot_connection(x1, y1, x2, y2, linestyle='dotted', color='blue'):
    plt.plot([x1, x2], [y1, y2], linestyle=linestyle, color=color)

def update(frame, R, r, p, x, y):
    plt.gca().clear()

    # 外円の描画
    outer_circle_theta = np.linspace(0, 2 * np.pi, 1000)
    plot_circle(R, outer_circle_theta)

    # 内円の描画
    inner_circle_theta = np.linspace(0, 2 * np.pi, 1000)
    inner_circle_x_offset = (R - r) * np.cos(theta[frame])
    inner_circle_y_offset = (R - r) * np.sin(theta[frame])
    plot_circle(r, inner_circle_theta, inner_circle_x_offset, inner_circle_y_offset)

    # ペン先と内円の中心を結んだ線分
    pen_x, pen_y = spirograph_xy(R, r, p, theta[frame])
    plot_connection(pen_x, pen_y, inner_circle_x_offset, inner_circle_y_offset)

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
speed = 1  # アニメーションのフレーム更新間隔（ミリ秒）

theta = spirograph_theta(R, r, n_points)
x, y = spirograph_xy(R, r, p, theta)

fig = plt.figure()
ani = FuncAnimation(fig, update, frames=range(n_points), fargs=(R, r, p, x, y), interval=speed, repeat=True)
plt.show()
