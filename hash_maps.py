"""
Ch 8. Blazing Fast Lookup With Hash Tables
"""

def exercise1(list1, list2):
    """
    Write a function that returns the intersection of two arrays.
    The intersection is a third array that contains all values contained within the first two arrays.
    For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].
    Your function should have a complexity of O(N).
    (If your programming language has a built-in way of doing this, don't use it.
    The idea is to build the algorithm yourself.)
    """
    dict1 = {entry: True for entry in list1}
    result = []

    for entry in list2:
        if dict1.get(entry):
            result.append(entry)

    return result

def exercise2(list1):
    """
    Write a function that accepts an array of strings and returns the first duplicate value it finds.
    For example, if the array is ["a", "b", "c", "d", "c", "e", "f"], the function should return "c",
    since it’s duplicated within the array. (You can assume that there’s one pair of duplicates within the array.)
    Make sure the function has an efficiency of O(N).
    """
    dict1 = {}

    for entry in list1:
        if dict1.get(entry):
            return entry
        else:
            dict1[entry] = True

def exercise3(string1):
    """
    Write a function that accepts a string that contains all the letters of the alphabet
    except one and returns the missing letter.
    For example, the string, "the quick brown box jumps over a lazy dog"
    contains all the letters of the alphabet except the letter, "f".
    The function should have a time complexity of O(N).
    """
    alphabet = {'a': False, "b": False, "c": False, "d": False, "e": False, "f": False, "g": False, "h": False, "i": False, "j": False, "k": False, "l": False, "m": False, "n": False, "o": False, "p": False, "q": False, "r": False, "s": False, "t": False, "u": False, "v": False, "w": False, "x": False, "y": False, "z":False}
    
    for entry in string1:
        alphabet[entry] = True

    for key, val in alphabet.items():
        if not val:
            return key


def exercise4(string1):
    """
    Write a function that returns the first non-duplicated character in a string.
    For example, the string, "minimum" has two characters that only exist once—the "n" and the "u",
    so your function should return the "n", since it occurs first. The function should have an efficiency of O(N).
    """
    dict1 = {}

    for entry in string1:
        if dict1.get(entry):
            dict1[entry] += 1
        else:
            dict1[entry] = 1

    for key, val in dict1.items():
        if val == 1:
            return key


list1 = [1, 2, 3, 4, 5]
list2 = [0, 2, 4, 6, 8]
test = exercise1(list1, list2)
print(f"exercise1 = {test}")

list1 = ["a", "b", "c", "d", "c", "e", "f"]
test = exercise2(list1)
print(f"exercise2 = {test}")

string1 = "the quick brown box jumps over a lazy dog"
test = exercise3(string1)
print(f"exercise3 = {test}")

string1 = "minimum"
test = exercise4(string1)
print(f"exercise4 = {test}")