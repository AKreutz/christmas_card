import numpy as np
import matplotlib.pyplot as plt


class Top:
    star_factor = 2*np.pi/5

    def __init__(self, x, y):
        center = np.array([x, y + 0.5])

        top = np.zeros(shape=(10, 2))
        for i in range(5):
            angle = self.star_factor * i + np.pi/2
            top[i*2] = center + np.array([np.cos(angle), np.sin(angle)])*0.5

        for i in range(5):
            angle = self.star_factor * i + np.pi/2 + self.star_factor/2
            top[i*2+1] = center + np.array([np.cos(angle), np.sin(angle)])*0.25
        self.top = np.array(top)

        self.base = np.array([
            [x - 0.1, y - 0.1],
            [x - 0.1, y + 0.5],
            [x + 0.1, y + 0.5],
            [x + 0.1, y - 0.1]
        ])

    def draw(self):
        plt.fill(self.top[:, 0], self.top[:, 1], color="#FFD700", zorder=9)
        plt.fill(self.base[:, 0], self.base[:, 1], color="#FFD700", zorder=9)
