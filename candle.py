import numpy as np
import matplotlib.pyplot as plt


class Candle:
    def __init__(self, x, y):
        self.candle = np.array([
            [x - 0.1, y],
            [x - 0.1, y + 0.7],
            [x + 0.1, y + 0.7],
            [x + 0.1, y]
        ])

        self.whick = np.array([
            [x, y + 0.7],
            [x, y + 0.8]
        ])

        self.flame = np.array([
            x, y + 0.85
        ])

    def draw(self):
        plt.fill(self.candle[:, 0], self.candle[:, 1], color="red", zorder=6)
        plt.plot(self.whick[:, 0], self.whick[:, 1], color="black", zorder=6)
        plt.scatter(self.flame[0], self.flame[1], color="yellow", zorder=6)
