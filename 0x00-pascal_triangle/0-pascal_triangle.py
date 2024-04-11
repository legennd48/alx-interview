#!/usr/bin/python3
"""Generates Pascal's triangle up to a given number of rows.

This module provides a function to generate Pascal's triangle, a mathematical
construct used in combinatorics. Pascal's triangle is an equilateral triangle
where each number is the sum of the two numbers directly above it.

The function takes a non-negative integer `n` as input and returns a list
of lists representing the rows of Pascal's triangle.

Args:
    n: The number of rows in the Pascal's triangle.

Returns:
    A list of lists containing the values of Pascal's triangle.

Raises:
    ValueError: If the number of rows is negative.
"""


def pascal_triangle(n):
    """Generates Pascal's triangle for a given number of rows.

    This function creates a list of lists representing Pascal's triangle
    for a given non-negative integer number of rows.

    Args:
        n: The number of rows in the Pascal's triangle.

    Returns:
        A list of lists containing the values of Pascal's triangle.

    Raises:
        ValueError: If the number of rows is negative.
    """

    if n < 0:
        raise ValueError("number of rows must be non-negative")

    pascal_triangle = []
    for row_index in range(n):
        row = []
        for col_index in range(row_index + 1):
            if col_index == 0 or col_index == row_index:
                row.append(1)
            elif row_index > 0 and col_index > 0:
                # Calculate the value at the current position using the values
                # from the previous row.
                previous_row = pascal_triangle[row_index - 1]
                value = previous_row[col_index - 1] + previous_row[col_index]
                row.append(value)
        pascal_triangle.append(row)

    return pascal_triangle
