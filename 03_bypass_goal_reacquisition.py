"""
Algorithm 3: Obstacle Bypass and Goal Reacquisition

Purpose:
    Manage state transitions after turning around an obstacle,
    then re-align the rover with the goal when the path is clear.
"""

from typing import Tuple


def bypass_and_reacquire(state: str,
                         d_front: float,
                         d_threshold: float,
                         goal_clear: bool,
                         theta_error: float,
                         v_max: float = 0.5,
                         omega_max: float = 0.8,
                         k: float = 1.0) -> Tuple[str, float, float]:
    """
    Update rover state during bypass and goal reacquisition.

    Returns:
        updated_state, linear_velocity, angular_velocity
    """
    v = 0.0
    omega = 0.0

    if state in {"Turn Left", "Turn Right"}:
        if d_front > d_threshold:
            state = "Bypass"
            v = v_max
            omega = omega_max if state == "Turn Left" else -omega_max
        else:
            omega = omega_max if state == "Turn Left" else -omega_max

    if state == "Bypass":
        v = v_max
        if goal_clear:
            state = "Goal Reacquire"
            omega = k * theta_error

    if state == "Goal Reacquire":
        v = v_max
        omega = k * theta_error

    return state, v, omega


if __name__ == "__main__":
    result = bypass_and_reacquire(
        state="Bypass",
        d_front=1.5,
        d_threshold=1.0,
        goal_clear=True,
        theta_error=0.15,
    )
    print(result)
