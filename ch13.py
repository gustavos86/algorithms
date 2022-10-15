"""
Exercises from Chapter 13 - Recursive Algorithms for Speed
"""

import sorting_algorithms as sa

def exercise01(list1):
    """
    Given an array of positive numbers, write a function that returns the greatest product of any three numbers.
    The approach of using three nested loops would clock in at O(N3), which is very slow.
    Use sorting to implement the function in a way that it computes at O(N log N) speed.
    (There are even faster implementations, but we're focusing on using sorting as a technique to make code faster.)
    """

    list1 = sa.quicksort(list1)

    return list1[-1] * list1[-2] * list1[-3]

def exercise02(list1):
    """
    The array is expected to have all integers from 0 up to the array's length, but one is missing.
    Return the missing number.
    """

    list1 = sa.quicksort(list1)

    for idx, val in enumerate(list1):
        if idx != val:
            return idx

def exercise03a(list1):
    """
    Write three different implementations of a function that finds the greatest number within an array.
    Write one function that is O(N2), one that is O(N log N), and one that is O(N).
    """
    for i in list1:
        i_is_the_gresatest = True
        for j in list1:
            if j > i:
                i_is_the_gresatest = False

        if i_is_the_gresatest:
            return i

def exercise03b(list1):
    """
    Write three different implementations of a function that finds the greatest number within an array.
    Write one function that is O(N2), one that is O(N log N), and one that is O(N).
    """

    list1 = sa.quicksort(list1)

    return list1[-1]

def exercise03c(list1):
    """
    Write three different implementations of a function that finds the greatest number within an array.
    Write one function that is O(N2), one that is O(N log N), and one that is O(N).
    """

    greatest_num_so_far = list1[0]
    for i in list1:
        if i > greatest_num_so_far:
            greatest_num_so_far = i

    return greatest_num_so_far