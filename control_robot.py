import os
from src.environment import Environment
from src.robot import Robot
from src.brick import Brick

def main():
    # Create a robot and environment
    robot = Robot(x=2.5, y=2.5)
    env = Environment(width=5, height=5, robot=robot)

    # Add some bricks for context
    env.add_brick(Brick(position=(1, 1), marker_id1=10, marker_id2=11))
    env.add_brick(Brick(position=(3, 2), marker_id1=12, marker_id2=13))
    env.add_brick(Brick(position=(4, 4), marker_id1=14, marker_id2=15))

    def redraw():
        os.system('clear' if os.name == 'posix' else 'cls')
        print("Robot Control")
        print("f: forward, l: left, r: right, q: quit")
        print(env.robot)
        env.visualize()

    redraw()

    while True:
        try:
            action = input("Enter action: ").lower()
            if action == 'f':
                robot.move_forward(0.5)
            elif action == 'l':
                robot.rotate_left(15)
            elif action == 'r':
                robot.rotate_right(15)
            elif action == 'q':
                break
            else:
                print("Invalid action.")
                continue

            redraw()

        except KeyboardInterrupt:
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()
