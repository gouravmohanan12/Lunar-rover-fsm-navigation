"""
Algorithm 2: FSM-Based Navigation Controller

Purpose:
    Use sector distances and a safety threshold to decide
    rover state and corresponding velocity command.
"""

from typing import Tuple


def fsm_navigation_controller(d_front: float,
                              d_left: float,
                              d_right: float,
                              d_threshold: float,
                              theta_error: float,
                              v_max: float = 0.5,
                              omega_max: float = 0.8,
                              k: float = 1.0) -> Tuple[str, float, float]:
    """
    Determine FSM state and control command.

    Returns:
        state, linear_velocity, angular_velocity
    """
    if d_front >= d_threshold:
        state = "Goal Seek"
        v = v_max
        omega = k * theta_error
    else:
        state = "Obstacle Detected"
        v = 0.0
        if d_left > d_right:
            state = "Turn Left"
            omega = omega_max
        else:
            state = "Turn Right"
            omega = -omega_max
    return state, v, omega


if __name__ == "__main__":
    result = fsm_navigation_controller(
        d_front=0.6,
        d_left=1.8,
        d_right=1.1,
        d_threshold=1.0,
        theta_error=0.2,
    )
    print(result)
