import math

class Robot:
    def __init__(self, x, y, heading=0.0):
        self.x = x
        self.y = y
        self.heading = heading  # Angle in radians

    def move_forward(self, distance):
        self.x += distance * math.cos(self.heading)
        self.y += distance * math.sin(self.heading)

    def rotate_left(self, angle_degrees):
        self.heading += math.radians(angle_degrees)

    def rotate_right(self, angle_degrees):
        self.heading -= math.radians(angle_degrees)

    def __repr__(self):
        return f"Robot(x={self.x:.2f}, y={self.y:.2f}, heading={math.degrees(self.heading):.2f}°)"
