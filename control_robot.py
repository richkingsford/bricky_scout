import os
from src.environment import Environment
from src.robot import Robot
from src.brick import Brick
from src.logger import SessionLogger

def main():
    # Create a robot, environment, and logger
    robot = Robot(x=2.5, y=2.5)
    env = Environment(width=5, height=5, robot=robot)
    logger = SessionLogger()

    # Add some bricks for context
    env.add_brick(Brick(position=(1, 1), marker_id1=10, marker_id2=11))
    env.add_brick(Brick(position=(3, 2), marker_id1=12, marker_id2=13))
    env.add_brick(Brick(position=(4, 4), marker_id1=14, marker_id2=15))

    def redraw(scan_results=None):
        os.system('clear' if os.name == 'posix' else 'cls')
        print("Robot Control")
        print("f: forward, l: left, r: right, s: scan, q: quit")
        print(env.robot)
        if scan_results:
            print("Scan Results:")
            if scan_results:
                for brick in scan_results:
                    print(f"  - {brick}")
            else:
                print("  No bricks detected.")
        env.visualize()

    redraw()

    while True:
        try:
            action = input("Enter action: ").lower()
            scan_results = None

            if action == 'f':
                robot.move_forward(0.5)
                logger.add_entry(action="move_forward", robot_pose=robot)
            elif action == 'l':
                robot.rotate_left(15)
                logger.add_entry(action="rotate_left", robot_pose=robot)
            elif action == 'r':
                robot.rotate_right(15)
                logger.add_entry(action="rotate_right", robot_pose=robot)
            elif action == 's':
                scan_results = env.scan()
                logger.add_entry(action="scan", robot_pose=robot, detections=scan_results)
            elif action == 'q':
                break
            else:
                print("Invalid action.")
                continue

            redraw(scan_results)

        except KeyboardInterrupt:
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()
