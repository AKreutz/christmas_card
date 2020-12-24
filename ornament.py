import numpy as np
import matplotlib.pyplot as plt


def random_position(segment):
    s, t = sorted(np.random.rand(2))
    return (s * segment[0] + (t - s) * segment[1] + (1 - t) * segment[2])


def distance(p1, p2):
    d = p1 - p2
    return np.sqrt(d[0]**2 + d[1]**2)


def calculate_score(position, positions):
    closest_to_others = 1000
    for p in positions:
        d = distance(position, p)
        if d < closest_to_others:
            closest_to_others = d

    return closest_to_others * 0.5


class Ornament:
    ALL_ORNAMENTS = []
    COLORS = {
        "#E40010": 0,  # RED
        "#C0C0C0": 0,  # SILVER
        "#FFD700": 0,  # GOLD
        "#022F89": 0,  # BLUE
        "#1FD537": 0   # GREEN
    }

    def __init__(self, segment, n_ornaments, radius=0.15):
        self.radius = radius
        self.ornaments = []
        self.hangers = []

        for position in self.get_positions(segment, n_ornaments):
            self.ornaments.append(position)

            self.hangers.append(np.array([
                position,
                position + np.array([0, 0.1])
            ]) + np.array([0, self.radius]))

        self.ALL_ORNAMENTS += self.ornaments

    def get_positions(self, segment, n_ornaments):
        candidate_positions = [random_position(segment) for i in range(1000)]
        center = (segment[0] + segment[1] + segment[2]) / 3

        positions = [center]
        while len(positions) < n_ornaments:
            best_position = None
            best_score = 0
            for position in candidate_positions:
                score = calculate_score(
                    position, positions + self.ALL_ORNAMENTS)
                if score > best_score:
                    best_score = score
                    best_position = position
            positions.append(best_position)
        return positions

    def draw(self):
        for i in range(len(self.ornaments)):
            least_frequent_color = 100000
            color = ""
            for key, value in self.COLORS.items():
                if value < least_frequent_color:
                    least_frequent_color = value
                    color = key
            self.COLORS[color] = self.COLORS[key] + 1

            plt.gca().add_artist(
                plt.Circle(
                    self.ornaments[i], self.radius, color=color, zorder=4)
            )
            plt.plot(
                self.hangers[i][:, 0],
                self.hangers[i][:, 1],
                color="black", zorder=5
            )
