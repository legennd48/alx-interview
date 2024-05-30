#!/usr/bin/python3

"""
This module defines a function to rotate a 2D matrix
90 degrees clockwise in-place.

Args:
    matrix: A 2D matrix represented as a list of lists.

Returns:
    None (modifies the matrix in-place).
"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix: A 2D matrix represented as a list of lists.

    Returns:
        None (modifies the matrix in-place).
    """

    n = len(matrix)

    # Layer-by-layer approach
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # Move left to right
            matrix[first][i] = matrix[last - offset][first]
            # Move bottom to top
            matrix[last - offset][first] = matrix[last][last - offset]
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            # Move top to left
            matrix[i][last] = top
