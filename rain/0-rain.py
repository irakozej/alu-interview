#!/usr/bin/python3


"""
Module: rain
"""


def rain(walls):
    """
    Calculate the total trapped water between walls.
    Args:
    walls (list): list of non-negative integers representing wall heights
    Returns:
    int: total trapped water.
    """

    if len(walls) == 0:
        return 0

    water = 0
    n = len(walls)

    for i in range(1, n - 1):
        left_max = max(walls[:i])
        right_max = max(walls[i + 1:])
        current_height = walls[i]
        min_boundary_height = min(left_max, right_max)

        if min_boundary_height > current_height:
            water += min_boundary_height - current_height

    return water
