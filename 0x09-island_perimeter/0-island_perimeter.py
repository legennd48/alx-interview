#!//usr/bin/python3
"""
Island Perimeter - Function
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in a grid.

    Args:
        grid: A list of lists of integers representing the grid.
              0 represents water, 1 represents land.

    Returns:
        The perimeter of the island as an integer.
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check all four neighbors (up, down, left, right)
                neighbors = [(row - 1, col), (row + 1, col),
                             (row, col - 1), (row, col + 1)]
                for neighbor_row, neighbor_col in neighbors:
                    # If neighbor is out of bounds or water, inc perimeter
                    if not (0 <= neighbor_row < rows and
                            0 <= neighbor_col < cols and
                            grid[neighbor_row][neighbor_col] == 1):
                        perimeter += 1

    return perimeter
