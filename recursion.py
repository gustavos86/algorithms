"""
Exercises from Ch 10
Recursively Recurse With Recursion
"""

def traverse_array(list1):
    """
    Traverse a list with multiple levels of deep using a recursive function
    """
    for value in list1:
        if isinstance(value, list):
            traverse_array(value)
        else:
            print(value, end=" ")

# Chapter 11

def ch11_exercise1(list1):
    """
    Use recursion to write a function that accepts an array of strings
    and returns the total number of characters across all the strings.
    For example, if the input array is ["ab", "c", "def", "ghij"],
    the output should be 10 since there are 10 characters in total.
    """
    if len(list1) == 1:
        return len(list1[0])
    else:
        return len(list1[0]) + ch11_exercise1(list1[1:])

def ch11_exercise2(list1):
    """
    Use recursion to write a function that accepts an array of numbers
    and returns a new array containing just the even numbers.
    """
    if not len(list1):
        return []

    if list1[0] % 2 == 0:
        # number is even
        tmp_list = list()
        tmp_list.append(list1[0])
        tmp_list.extend(ch11_exercise2(list1[1:]))
        return tmp_list
    else:
        # number is odd
        return list(ch11_exercise2(list1[1:]))

def ch11_exercise3(n):
    """
    There is a numerical sequence known as “Triangular Numbers.”
    The pattern begins as 1, 3, 6, 10, 15, 21, and continues onward with the Nth number in the pattern,
    which is N plus the previous number. For example, the 7th number in the sequence is 28, since it’s 7
    (which is N) plus 21 (the previous number in the sequence).
    Write a function that accepts a number for N and returns the correct number from the series.
    That is, if the function was passed the number 7, the function would return 28.
    """
    if n == 1:
        return 1
    else:
        return n + ch11_exercise3(n - 1)

def ch11_exercise4(string1, counter=0):
    """
    Use recursion to write a function that accepts a string and returns the first index that contains the character “x.”
    For example, the string, "abcdefghijklmnopqrstuvwxyz" has an “x” at index 23.
    To keep things simple, assume the string definitely has at least one “x.”
    """
    if string1[0] == 'x':
        return counter
    else:
        return ch11_exercise4(string1[1:], counter + 1)
