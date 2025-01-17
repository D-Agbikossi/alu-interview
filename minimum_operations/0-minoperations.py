#!/usr/bin/python3
""" Script that computes a minimum operations
    needed in a CopyAll - Paste task.
"""


def minOperations(n):
    """
    A method that calculates the fewest number
    of operations needed to result in exactly n
    H characters in the file.

    Args:
        n (int): input value for the task

    Return:
        int: the minimum number of operations required to achieve exactly n 'H' characters.
        If it is impossible to achieve, return 0.
    """
    if n < 2:
        return 0

    operations = 0
    i = 2  # because 1 is not a valid factor

    # Factorize n and sum the necessary operations
    while i * i <= n:  # We only need to check up to sqrt(n)
        while n % i == 0:
            operations += i  # Add the factor to operations
            n //= i  # Divide n by the factor
        i += 1

    # If n > 1, it means n itself is a prime factor
    if n > 1:
        operations += n

    return operations

