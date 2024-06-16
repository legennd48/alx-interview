#!/usr/bin/python3
'''
Prime Game
'''


def isWinner(x, nums):
    """Determine the winner of the most rounds of the prime game."""
    if not nums or x <= 0:
        return None

    # Function to determine prime numbers using Sieve of Eratosthenes
    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_numbers

    max_n = max(nums)
    primes = sieve(max_n)

    def game_winner(n):
        multiples = [False] * (n + 1)
        moves = 0
        for prime in primes:
            if prime > n:
                break
            if not multiples[prime]:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    multiples[multiple] = True
        return moves % 2  # Maria wins if moves are odd, Ben if even

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if game_winner(n) == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
