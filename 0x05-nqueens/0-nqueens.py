#!/usr/bin/python3
"""N queens solution finder module.

This module finds all solutions to the N-queens problem, where N queens
are placed on an N x N chessboard such that no two queens threaten each other.

The solution representation is a list of lists, where each inner list
contains the row and column coordinates of a queen.

This module uses a backtracking approach to solve the problem.
"""
import sys


solutions = []
"""The list to store all valid solutions found for the N-queens problem."""

n = 0
"""The size of the chessboard (number of rows and columns)."""

pos = None
"""A pre-computed list containing all possible positions on the chessboard
(represented as row-column pairs)."""


def get_input():
  """Retrieves and validates the program's argument (chessboard size).

  Returns:
    int: The size of the chessboard (N).

  Exits:
    The program exits with an error message and status code 1 if:
      - The number of arguments is incorrect (must be exactly 2).
      - The provided N is not a valid integer.
      - N is less than 4 (the minimum board size for the N-queens problem).
  """

  global n
  n = 0

  if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number")
    sys.exit(1)

  if n < 4:
    print("N must be at least 4")
    sys.exit(1)

  return n


def is_attacking(pos0, pos1):
  """
  Checks if two queens placed at the given positions threaten each other.

  Args:
    pos0 (list or tuple): The first queen's position as [row, col].
    pos1 (list or tuple): The second queen's position as [row, col].

  Returns:
    bool: True if the queens are attacking each other (on the same row,
          column, or diagonal), False otherwise.
  """

  return (pos0[0] == pos1[0] or  # Same row
          pos0[1] == pos1[1] or  # Same column
          abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))  # Diagonal attack


def group_exists(group):
  """
  Checks if a group of queen positions already exists in the list of solutions.

  Args:
    group (list of list of int): A group of queen positions as [[row, col], ...].

  Returns:
    bool: True if the group is found in the solutions list (after sorting
          both for comparison), False otherwise.
  """

  global solutions
  for sol in solutions:
    if sorted(sol) == sorted(group):
      return True
  return False


def build_solution(row, group):
  """
  Recursively builds solutions for the N queens problem using backtracking.

  Args:
    row (int): The current row being considered for queen placement.
    group (list of list of int): The current group of valid queen positions.
  """

  global solutions, n

  if row == n:  # Reached the last row, a complete solution is found
    tmp0 = group.copy()
    if not group_exists(tmp0):
      solutions.append(tmp0)
  else:
    for col in range(n):
      new_pos = [row, col]  # Candidate position for a queen in the current row
      if all(not is_attacking(new_pos, pos) for pos in group):  # Check for attacks
        group.append(new_pos)  # Add the candidate position to the current solution
        build_solution(row + 1, group)  # Recursively explore next row
        group.pop()  # Backtrack: remove the candidate if it doesn't lead to a solution


def get_solutions():
  """
  Generates all solutions for the N queens problem based on the chessboard size.

  This function populates the 'solutions' list with all valid solutions
  (queen placements) for the N-queens problem on an N x N chessboard.
  """
    global pos, n
    pos = [[i // n, i % n] for i in range(n ** 2)]
    build_solution(0, [])

n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
