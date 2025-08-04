from src.environment import Environment
from src.brick import Brick

def main():
    # Create a 5x5 environment
    env = Environment(5, 5)

    # Add some bricks
    env.add_brick(Brick(position=(1, 1), marker_id1=10, marker_id2=11))
    env.add_brick(Brick(position=(3, 2), marker_id1=12, marker_id2=13))
    env.add_brick(Brick(position=(4, 4), marker_id1=14, marker_id2=15))

    # Visualize the environment
    env.visualize()

if __name__ == "__main__":
    main()
