import random

class Brick:
    def __init__(self, position, marker_id1, marker_id2):
        self.position = position
        self.marker_ids = [marker_id1, marker_id2]

    def __repr__(self):
        return f"Brick(position={self.position}, markers={self.marker_ids})"
