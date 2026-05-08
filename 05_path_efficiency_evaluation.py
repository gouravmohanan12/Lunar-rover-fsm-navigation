"""
Algorithm 5: Path Efficiency Evaluation

Purpose:
    Compute path efficiency as the ratio between optimal
    straight-line distance and actual travelled distance.
"""


def compute_path_efficiency(d_optimal: float, d_actual: float) -> float:
    """
    Compute path efficiency.

    Args:
        d_optimal: Straight-line distance from start to goal.
        d_actual: Actual distance travelled by the rover.

    Returns:
        Efficiency value eta.
    """
    if d_actual <= 0:
        raise ValueError("Actual distance must be greater than zero.")
    return d_optimal / d_actual


if __name__ == "__main__":
    eta = compute_path_efficiency(d_optimal=10.0, d_actual=13.5)
    print(f"Path efficiency: {eta:.3f}")
