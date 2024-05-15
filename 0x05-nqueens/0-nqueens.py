#!/usr/bin/python3
"""
0. N queens
"""
import sys

solutions = []
"""
The list to contain possible solutions
to the N queens problem.
"""
board_size = 0
"""
The size of the chessboard.
"""
positions = None
"""
The list of possible positions on the chessboard.
"""


def parse_arguments():
    """
    Retrieve and validate the program's argument.

    Returns:
        int: The size of the chessboard (board_size).

    Exits:
        If the number of arguments is incorrect or if board_size is
        not a valid integer >= 4.
    """
    global board_size
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def queens_attack_each_other(queen1, queen2):
    """
    Check if two queens are in an attacking position.

    Args:
        queen1 (list or tuple): The first queen's position as [row, col].
        queen2 (list or tuple): The second queen's position as [row, col].

    Returns:
        bool: True if the queens are in an attacking position, otherwise False.
    """
    return (queen1[0] == queen2[0] or
            queen1[1] == queen2[1] or
            abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]))


def solution_exists(candidate_solution):
    """
    Check if a candidate solution exists in the list of solutions.

    Args:
        candidate_solution (list of list of int):
            A candidate solution as [[row, col], ...].

    Returns:
        bool: True if the candidate solution exists in solutions,
        otherwise False.
    """
    global solutions
    for solution in solutions:
        if sorted(solution) == sorted(candidate_solution):
            return True
    return False


def find_solutions(row, current_solution):
    """
    Recursively build solutions for the N queens problem.

    Args:
        row (int): The current row being considered.
        current_solution (list of list of int): The current
        group of valid queen positions.
    """
    global solutions, board_size
    if row == board_size:
        solution_copy = current_solution.copy()
        if not solution_exists(solution_copy):
            solutions.append(solution_copy)
    else:
        for col in range(board_size):
            new_position = [row, col]
            if all(not queens_attack_each_other(new_position, queen)
                   for queen in current_solution):
                current_solution.append(new_position)
                find_solutions(row + 1, current_solution)
                current_solution.pop()


def generate_solutions():
    """
    Generate all solutions for the N queens problem
    based on the chessboard size.
    """
    global positions, board_size
    positions = [
        [i // board_size, i % board_size] for i in range(board_size ** 2)
        ]
    find_solutions(0, [])


board_size = parse_arguments()
generate_solutions()
for solution in solutions:
    print(solution)
