"""
Exercises from Chapter 12 - Dynamic Programming
"""

def add_until_100(array):
    """
    The following function accepts an array of numbers and returns the sum,
    as long as a particular number doesn't bring the sum above 100.
    If adding a particular number will make the sum higher than 100,
    that number is ignored. However, this function makes unnecessary recursive calls.
    Fix the code to eliminate the unnecessary recursion:
    """
    if len(array) == 0:
        return 0

    sumOfRemainingNumbers = add_until_100(array[1:])

    if array[0] + sumOfRemainingNumbers > 100:
        return sumOfRemainingNumbers
    else:
        return array[0] + sumOfRemainingNumbers

def golomb(n, memo={}):
    """
    The following function uses recursion to calculate the Nth number from
    a mathematical sequence known as the “Golomb sequence.”
    It's terribly inefficient, though! Use memoization to optimize it.
    (You don't have to actually understand how the Golomb sequence works to do this exercise.)
    """
    if n == 1:
        return 1
    
    if not memo.get(n):
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    
    return memo[n]

def unique_paths(rows, columns, memo={}):
    """
    Here is a solution to the “Unique Paths” problem from an exercise in the previous chapter.
    Use memoization to improve its efficiency:
    """
    if rows == 1 or columns == 1:
        return 1

    if not memo.get((rows, columns)):
        memo[(rows, columns)] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)

    return memo[(rows, columns)]