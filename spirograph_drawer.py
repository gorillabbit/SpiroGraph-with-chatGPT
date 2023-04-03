import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def spirograph_theta(R, r, angular_speed_ratio=1):
    n_points = 1000
    return np.linspace(0, 2 * np.pi * abs(r / np.gcd(R, r)) * angular_speed_ratio, n_points)


def spirograph_xy(R, r, p, theta):
    x = (R - r) * np.cos(theta) + p * np.cos(((R - r) / r) * theta)
    y = (R - r) * np.sin(theta) - p * np.sin(((R - r) / r) * theta)
    return x, y

def plot_circle(radius, theta, x_offset=0, y_offset=0):
    x = x_offset + radius * np.cos(theta)
    y = y_offset + radius * np.sin(theta)
    plt.plot(x, y, linestyle='dashed', color='gray')

def plot_connection(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], linestyle='dotted', color='blue')

def update(frame, R, r, p, x, y, theta):
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

def draw_animation(fig, R, r, p, angular_speed_ratio):
    theta = spirograph_theta(R, r, angular_speed_ratio)
    x, y = spirograph_xy(R, r, p, theta)
    anim = FuncAnimation(fig, update, frames=1000, fargs=(R, r, p, x, y, theta), interval=50)
    return anim

def close_animation():
    plt.cla()