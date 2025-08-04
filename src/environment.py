import matplotlib.pyplot as plt
import matplotlib.patches as patches
from src.brick import Brick

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bricks = []

    def add_brick(self, brick):
        if 0 <= brick.position[0] < self.width and 0 <= brick.position[1] < self.height:
            self.bricks.append(brick)
        else:
            raise ValueError("Brick position is outside the environment boundaries.")

    def visualize(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_xticks(range(self.width + 1))
        ax.set_yticks(range(self.height + 1))
        ax.grid(True)

        for brick in self.bricks:
            x, y = brick.position
            rect = patches.Rectangle((x, y), 1, 1, linewidth=1, edgecolor='r', facecolor='r', alpha=0.5)
            ax.add_patch(rect)
            ax.text(x + 0.5, y + 0.5, f"B{brick.marker_ids[0]}/{brick.marker_ids[1]}",
                    ha='center', va='center', color='white')

        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

    def __repr__(self):
        return f"Environment(width={self.width}, height={self.height}, bricks={len(self.bricks)})"
