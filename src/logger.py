import datetime

class SessionLogger:
    def __init__(self):
        self.log = []

    def add_entry(self, action, robot_pose, detections=None):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "action": action,
            "robot_pose": {
                "x": robot_pose.x,
                "y": robot_pose.y,
                "heading": robot_pose.heading
            },
            "detections": []
        }
        if detections:
            for brick in detections:
                entry["detections"].append({
                    "marker_ids": brick.marker_ids,
                    "position": brick.position
                })
        self.log.append(entry)

    def get_log(self):
        return self.log

    def __repr__(self):
        return f"SessionLogger(entries={len(self.log)})"
