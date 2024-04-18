#!/usr/bin/python3
'''
This module is an attempt to solve a problem
with locked boxes
'''


def canUnlockAll(boxes):
    """
    Check if a list of locked boxes can be unlocked.

    Receives a list of boxes as an argument and returns True or False
    based on whether all boxes in the list can be unlocked.

    Args:
    - boxes (list): A list of lists where each inner list
    contains keys to other boxes.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    seen_boxes = {0}
    unseen_boxes = set(boxes[0]).difference({0})
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)

    return n == len(seen_boxes)
