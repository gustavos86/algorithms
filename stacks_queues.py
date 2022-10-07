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

    def __len__(self):
        """
        Returns the number of elements in the stack
        """
        return len(self.list1)

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

def linter(string1):
    """
    Inspects a line of JavaScript, C, etc code and
    ensures that there are no brace-related syntax errors
    """
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = Stack()

    for char in string1:
        if char in braces.keys():
            stack.push(char)
        elif char in braces.values():
            if len(stack):
                brace = stack.pop()
            else:
                # There are no elements in the stack to pop...
                # There are more closing than opening braces
                print("ERROR: Braces do not match")
                print("There are more closing than opening braces")
                return

            if braces[brace] != char:
                # the elements do not match!
                # The opening does not match with the closing brace
                print("ERROR: Braces do not match")
                print("The opening does not match with the closing brace")
                return

    if not len(stack):
        print("GOOD: All braces have a match!")
    else:
        # There are leftovers in the stack...
        # There are more opening than closing braces
        print("ERROR: Braces do not match")
        print("There are more opening than closing braces")
        return

    

test = "(var x = {y: [1, 2, 3]})"
linter(test)  # Should be "GOOD: All braces have a match!"

test = "var x = {y: [1, 2, 3]})"
linter(test)  # Should be ERROR "There are more closing than opening braces"

test = "(var x = y: [1, 2, 3]})"
linter(test)  # Should be ERROR "The opening does not match with the closing brace"

test = "(var x = {y: 1, 2, 3]})"
linter(test)  # Should be ERROR "The opening does not match with the closing brace"

test = "(var x = {y: [1, 2, 3})"
linter(test)  # Should be ERROR "The opening does not match with the closing brace"

test = "(var x = {y: [1, 2, 3])"
linter(test)  # Should be ERROR "The opening does not match with the closing brace"

test = "(var x = {y: [1, 2, 3]}"
linter(test)  # Should be ERROR "There are more opening than closing braces"

test = "(var x = {y: [1, 2, 3]}))"
linter(test)  # Should be ERROR "There are more closing than opening braces"

test = "((var x = {y: [1, 2, 3]})"
linter(test)  # Should be ERROR "There are more opening than closing braces"