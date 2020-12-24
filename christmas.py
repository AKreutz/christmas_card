import numpy as np
import matplotlib.pyplot as plt

from candle import Candle
from lametta import Lametta
from top import Top
from ornament import Ornament


class ChristmasTree:
    def __init__(self, segments=10):
        self.make_tree(segments)
        self.make_decoration()

    def make_tree(self, segments):
        self.segments = []
        total_height = 0
        for height in range(1, segments + 1):
            segment = self.make_segment(height, total_height)
            self.segments.append(segment)
            total_height += height/2
        self.make_stem(total_height + height/2)

    def make_segment(self, height, total_height):
        width = height * 2.5
        segment = np.array([
                [-width/2, -height],
                [width/2, -height],
                [0, 0]
            ])
        segment[:, 1] -= total_height
        return segment

    def make_stem(self, total_height):
        stem_width = total_height/10
        stem_max = -total_height
        stem_min = -total_height - total_height/6

        self.stem = np.array([
            [-stem_width/2, stem_max],
            [-stem_width/2, stem_min],
            [stem_width/2, stem_min],
            [stem_width/2, stem_max]
        ])

    def make_decoration(self):
        self.make_candles()
        self.make_top()
        self.make_lametta()
        self.make_ornaments()

    def make_candles(self):
        self.candles = []
        for i, segment in enumerate(self.segments):
            distance = segment[1, 0] - segment[0, 0]
            y = (segment[2, 1] - segment[0, 1])/16 + segment[0, 1]

            self.candles.append(Candle(segment[0, 0] + distance/8, y))
            self.candles.append(Candle(segment[1, 0] - distance/8, y))

            if i < 5:
                n_intermediate_candles = min(i + 1, 3)
            elif i == 5:
                n_intermediate_candles = 4

            for j in range(n_intermediate_candles):
                d = (distance - distance/4) / n_intermediate_candles
                self.candles.append(
                    Candle(segment[0, 0] + distance/8 + (j + 1) * d, y)
                )

    def make_top(self):
        x, y = self.segments[0][2]
        self.top = Top(x, y)

    def make_lametta(self):
        self.lamettas = []
        for segment in self.segments:
            left_point = segment[0] + (segment[2] - segment[0])*0.4
            right_point = segment[1] + (segment[2] - segment[1])*0.4
            self.lamettas.append(Lametta(left_point, right_point))

    def make_ornaments(self):
        self.ornaments = []
        all_ornaments = []
        for i, segment in enumerate(self.segments):
            self.ornaments.append(Ornament(segment, i*4, 0.18))
            all_ornaments += self.ornaments[-1].ornaments

    def draw(self):
        plt.fill(self.stem[:, 0], self.stem[:, 1], color="#663300", zorder=2)

        for segment in self.segments:
            plt.fill(segment[:, 0], segment[:, 1], color="#004800", zorder=1)

        for candle in self.candles:
            candle.draw()

        for lametta in self.lamettas:
            lametta.draw()

        for ornament in self.ornaments:
            ornament.draw()

        self.top.draw()

        plt.text(
            x=0, y=2,
            s="F r o h e   W e i h n a c h t e n",
            horizontalalignment="center",
            fontsize=30,
            color="white",
            zorder=20
        )


if __name__ == "__main__":
    fig = plt.figure(figsize=(10, 10))
    christmas_tree = ChristmasTree(6)
    christmas_tree.draw()
    fig.canvas.draw()
    plt.axis("equal")
    plt.gca().set_ylim([-17.5, 4])

    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    plt.xticks([])
    plt.yticks([])

    plt.gca().set_facecolor("#0C1445")
    plt.savefig(
        "christmas_card.png", bbox_inches="tight", pad_inches=0,
        facecolor="#0C1445", edgecolor="#0C1445"
    )
    plt.show()
