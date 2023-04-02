import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def spirograph_coords(R, r, p, n_points=1000):
    theta = np.linspace(0, 2 * np.pi * abs((r * 1.0) / np.gcd(R, r)), n_points)
    x = (R - r) * np.cos(theta) + p * np.cos(((R - r) / r) * theta)
    y = (R - r) * np.sin(theta) - p * np.sin(((R - r) / r) * theta)
    return x, y

def update(frame, R, r, p, x, y):
    plt.gca().clear()
    plt.gca().set_aspect('equal', adjustable='box')

    outer_circle = R * np.array([np.cos(frame), np.sin(frame)])
    inner_circle = (R - r) * np.array([np.cos(frame), np.sin(frame)]) + r * np.array([np.cos((R - r) * frame / r), np.sin((R - r) * frame / r)])

    plt.plot(*outer_circle, 'o', color='gray')
    plt.plot(*inner_circle, 'o', color='gray')

    plt.plot(*np.column_stack((outer_circle, inner_circle)), color='blue', linestyle='dotted')

    plt.plot(x[:frame], y[:frame])

    plt.title(f'Spirograph (R={R}, r={r}, p={p})')

R = 100
r = 75
p = 50
n_points = 1000
speed = 50

x, y = spirograph_coords(R, r, p, n_points)
theta = np.linspace(0, 2 * np.pi * abs((r * 1.0) / np.gcd(R, r)), n_points)

fig = plt.figure()
ani = FuncAnimation(fig, update, frames=range(n_points), fargs=(R, r, p, x, y), interval=speed, repeat=True)
plt.show()
