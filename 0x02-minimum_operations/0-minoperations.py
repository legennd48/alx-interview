#!/usr/bin/python3
'''
Coding challenge to find
the minimum number of operations
for a task.
'''


def minOperations(n):
    """
    Calculates the minimum number of operations
    required to achieve a string
    of length `target_length` consisting
    only of the character 'H'.

    This function simulates copying and pasting
    operations to efficiently generate
    the target string.
    Args:
        n: The desired length of the final string.
    Returns:
        The minimum number of operations required to
        achieve the target length.
    Raises:
        TypeError: If the provided target_length
        is not an integer.
    """

    if not isinstance(n, int):
        return 0

    number_of_operations = 0
    clipboard_content = 0
    current_length = 1

    while current_length < n:
        if clipboard_content == 0:
            # Initialize by copying all existing characters and pasting
            clipboard_content = current_length
            current_length += clipboard_content
            number_of_operations += 2
        elif n - current_length > 0 and (n -
                                         current_length) % current_length == 0:
            # Copy all and paste if it results in the target length
            clipboard_content = current_length
            current_length += clipboard_content
            number_of_operations += 2
        elif clipboard_content > 0:
            # Paste the clipboard content
            current_length += clipboard_content
            number_of_operations += 1

    return number_of_operations
