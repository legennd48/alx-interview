#!/usr/bin/python3
"""
Change making module.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.

    Args:
        coins (List[int]): A list of integers representing the values of
        available coins (each value greater than 0).
        total (int): An integer representing the target
        amount to make change for.

    Returns:
        int: The fewest number of coins needed to reach the `total` amount or
        0 if `total` is 0 or less, or -1 if the `total` cannot be met with any
        combination of coins.
    """
    # If total is 0 or negative, no coins are needed
    if total <= 0:
        return 0

    # Sort the coins in descending order to use the largest coins first
    sorted_coins = sorted(coins, reverse=True)
    coins_count = 0  # Counter for the number of coins used

    # Iterate through the sorted coins
    for coin in sorted_coins:
        # If the total has been met, exit the loop
        if total <= 0:
            break
        # If the current coin can be used
        if coin <= total:
            # Determine the maximum number of this coin that can be used
            num_coins = total // coin
            # Subtract the equivalent amount from the total
            total -= num_coins * coin
            # Add the number of coins used to the count
            coins_count += num_coins

    # If the total is 0, return the coin count; otherwise, return -1
    return coins_count if total == 0 else -1
