import numpy as np
import matplotlib.pyplot as plt


def distance(p1, p2):
    d = p1 - p2
    return np.sqrt(d[0]**2 + d[1]**2)


class Lametta:
    def __init__(self, left, right):
        x_diff = right[0] - left[0]
        lametta = []
        self.bristles = []
        prev_point = -np.array([float("inf"), float("inf")])
        for x in np.linspace(left[0], right[0], 100):
            y = left[1] + ((x/x_diff)**2 - 0.25)*x_diff*0.5
            lametta.append(np.array([x, y]))

            if distance(prev_point, np.array([x, y])) > 0.2:
                prev_point = np.array([x, y])

                for i in range(3):
                    angle = np.arctan(x/x_diff) + 2*np.pi/3 * i
                    normal = np.array([np.cos(angle), np.sin(angle)]) * 0.05
                    self.bristles.append(np.array([
                        np.array([x, y]) - normal,
                        np.array([x, y]) + normal
                    ]))

        self.lametta = np.array(lametta)

    def draw(self):
        plt.plot(
            self.lametta[:, 0], self.lametta[:, 1], color="white", zorder=3)
        for bristle in self.bristles:
            plt.plot(bristle[:, 0], bristle[:, 1], color="white", zorder=3)
