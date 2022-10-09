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
            