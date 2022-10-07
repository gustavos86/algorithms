"""
Exercise from Chapter
9. Crafting Elegant Code With Stacks And Queues
"""

class Stack:
    """
    Abstract data structure Stack
    Uses an array in the backend
    """
    def __init__(self):
        """
        Initializes an empty stack
        """
        self.list1 = []

    def push(self, item):
        """
        Pushes an item on the Stack
        """
        self.list1.append(item)

    def pop(self):
        """
        Removes an item from the stack
        """
        return self.list1.pop()

def reverse_string(string1):
    """
    Write a function that uses a stack to reverse a string.
    (For example, "abcde" would become "edcba".)
    You can work with our earlier implementation of the Stack class.
    """
    stack = Stack()
    for letter in string1:
        stack.push(letter)

    reversed_string = ""
    for letter in range(len(string1)):
        reversed_string += stack.pop()

    return reversed_string

test = reverse_string("abcde")
print(f"reverse_string {test}")