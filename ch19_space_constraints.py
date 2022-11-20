"""
Chapter 19
Dealing with Space Constraints

Exercises
The following exercises provide you with the opportunity to practice with space constraints.
"""
def question3():
    """
    Create a new function to reverse an array that takes up just O(1) extra space.
    """
    def solution(array):
        middle_idx = len(array) // 2
        init = 0
        last = -1
        for _dummy in range(middle_idx):
            array[init], array[last] = array[last], array[init]
            init += 1
            last -= 1

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(f"Originnal array {array}")
    solution(array)
    print(f"Reversed array  {array}")

question3()