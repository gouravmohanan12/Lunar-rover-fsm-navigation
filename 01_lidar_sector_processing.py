"""
Algorithm 1: Sector-Based LiDAR Processing

Purpose:
    Divide LiDAR scan data into front, left, and right sectors,
    then compute the minimum distance in each sector.
"""

from typing import Iterable, Tuple


def process_lidar_sectors(front_sector: Iterable[float],
                          left_sector: Iterable[float],
                          right_sector: Iterable[float]) -> Tuple[float, float, float]:
    """
    Compute minimum distances in three LiDAR sectors.

    Args:
        front_sector: LiDAR ranges in the front angular sector.
        left_sector: LiDAR ranges in the left angular sector.
        right_sector: LiDAR ranges in the right angular sector.

    Returns:
        A tuple of (d_front, d_left, d_right).
    """
    d_front = min(front_sector)
    d_left = min(left_sector)
    d_right = min(right_sector)
    return d_front, d_left, d_right


if __name__ == "__main__":
    front = [1.8, 1.2, 0.9, 1.4]
    left = [2.2, 2.5, 2.0, 1.9]
    right = [1.3, 1.1, 1.7, 1.5]
    print(process_lidar_sectors(front, left, right))
