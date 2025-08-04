import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from src.brick import Brick
from src.robot import Robot

class Environment:
    def __init__(self, width, height, robot=None):
        self.width = width
        self.height = height
        self.bricks = []
        self.robot = robot

    def add_brick(self, brick):
        if 0 <= brick.position[0] < self.width and 0 <= brick.position[1] < self.height:
            self.bricks.append(brick)
        else:
            raise ValueError("Brick position is outside the environment boundaries.")

    def scan(self, max_view_distance=4.0):
        if not self.robot:
            return []

        detected_bricks = []
        robot_pos = (self.robot.x, self.robot.y)
        fov_rad = math.radians(self.robot.fov_deg)

        for brick in self.bricks:
            brick_center = (brick.position[0] + 0.5, brick.position[1] + 0.5)

            # Vector from robot to brick
            vec_x = brick_center[0] - robot_pos[0]
            vec_y = brick_center[1] - robot_pos[1]

            # Distance to brick
            distance = math.sqrt(vec_x**2 + vec_y**2)

            if distance > max_view_distance:
                continue

            # Angle to brick
            angle_to_brick = math.atan2(vec_y, vec_x)

            # Normalize angles to be within [-pi, pi]
            robot_heading = self.robot.heading % (2 * math.pi)
            if robot_heading > math.pi:
                robot_heading -= 2 * math.pi

            angle_diff = angle_to_brick - robot_heading
            # Normalize angle_diff to be within [-pi, pi]
            if angle_diff > math.pi:
                angle_diff -= 2 * math.pi
            elif angle_diff < -math.pi:
                angle_diff += 2 * math.pi

            if abs(angle_diff) <= fov_rad / 2:
                detected_bricks.append(brick)

        return detected_bricks

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

        if self.robot:
            import math
            # Draw robot
            robot_patch = patches.Circle((self.robot.x, self.robot.y), radius=0.4, color='blue', alpha=0.7)
            ax.add_patch(robot_patch)
            # Draw heading line
            ax.plot([self.robot.x, self.robot.x + 0.5 * math.cos(self.robot.heading)],
                    [self.robot.y, self.robot.y + 0.5 * math.sin(self.robot.heading)],
                    color='black', linewidth=2)

        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

    def __repr__(self):
        return f"Environment(width={self.width}, height={self.height}, bricks={len(self.bricks)}, robot={self.robot})"
