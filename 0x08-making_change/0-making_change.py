#!/usr/bin/python3
'''
MakeChange
'''


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to make
    change for a given amount using dynamic programming.

    Args:
      coins (List[int]): A list of integers representing
      the values of available coins (each value greater than 0).
      total (int): An integer representing the target
      amount to make change for.

    Returns:
      int: The fewest number of coins needed to reach the
      `total` amount or 0 if `total` is 0 or less, or -1 if the
      `total` cannot be met with any combination of coins.
    """

    if not all(coin > 0 for coin in coins):
        raise ValueError("Coin values must be integers greater than 0.")

    # Efficiently sort coins in descending 
    coins.sort(reverse=True)

    # Create a table to store minimum coin counts for all amounts up to `total`
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 amount requires 0 coins

    # Iterate through all possible amounts up to `total`
    for amount in range(1, total + 1):
        # Consider using each coin in descending order
        for coin in coins:
            # If the coin value is less than or equal to the current amount
            if coin <= amount:
                # Update `dp[amount]`
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
                if dp[amount] != float('inf'):
                    break

    # Return the minimum coin count for the target amount (`total`)
    return dp[total] if dp[total] != float('inf') else -1
