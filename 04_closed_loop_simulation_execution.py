"""
Algorithm 4: Closed-Loop Simulation Execution

Purpose:
    Represent the full rover simulation loop from LiDAR sensing
    to FSM decision-making, actuation, and odometry logging.
"""

from time import sleep


def run_closed_loop_simulation(max_steps: int = 10) -> None:
    """
    Demonstration of the sensing-control-motion loop.
    This is pseudocode-style Python for documentation purposes.
    """
    for step in range(max_steps):
        # 1. Gazebo generates LiDAR scan data
        lidar_scan = f"scan_data_step_{step}"

        # 2. ROS 2 publishes sensor data on /scan
        # 3. Controller subscribes to /scan and processes it
        state = "Goal Seek" if step < 5 else "Obstacle Detected"

        # 4. Controller publishes velocity command on /cmd_vel
        cmd_vel = {"linear": 0.5 if state == "Goal Seek" else 0.0,
                   "angular": 0.0 if state == "Goal Seek" else 0.8}

        # 5. Gazebo updates rover motion
        # 6. Odometry is published on /odom
        odom = f"odom_step_{step}"

        # 7. Logger records rover trajectory
        print({
            "step": step,
            "scan": lidar_scan,
            "state": state,
            "cmd_vel": cmd_vel,
            "odom": odom,
        })
        sleep(0.05)


if __name__ == "__main__":
    run_closed_loop_simulation()
