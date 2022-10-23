"""
Exercises from Ch 15 - Speeding Up All The Things With Binary Search Trees
"""
class TreeNode:
    def __init__(self, val,left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

def insert(value, node):
    if value < node.value:

        # If the left child does not exist, we want to insert
        # the value as the left child:
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insert(value, node.leftChild)

    elif value > node.value:

        # If the right child does not exist, we want to insert
        # the value as the right child:
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.rightChild)

def traverse_and_print_inorder(node):
    """
    inorder print
    """
    if node is None:
        return
    traverse_and_print_inorder(node.leftChild)
    print(node.value)
    traverse_and_print_inorder(node.rightChild)

def traverse_and_print_preorder(node):
    """
    Exercise 4
    In the text I demonstrated how to use inorder traversal to print a list of all the book titles.
    Another way to traverse a tree is known as preorder traversal.
    Here is the code for it as applied to our book app:
    """
    if node is None:
        return
    print(node.value)
    traverse_and_print_preorder(node.leftChild)
    traverse_and_print_preorder(node.rightChild)

def traverse_and_print_postorder(node):
    """
    Exercise 5
    There is yet another form of traversal called postorder traversal. Here is the code as applied to our book app:
    For the example tree in the text (which also appears in the previous exercise),
    write out the order in which the book titles are printed with postorder traversal.
    """
    if node is None:
        return
    traverse_and_print_postorder(node.leftChild)
    traverse_and_print_postorder(node.rightChild)
    print(node.value)

def find_greatest_value(node):
    """
    Exercise 3
    Write an algorithm that finds the greatest value within a binary search tree.
    """
    if node.rightChild:
        return find_greatest_value(node.rightChild)
    else:
        return node.value

# Fill the Binary Search Tree
elements_to_insert = [1, 5, 9, 2, 4, 10, 6, 3, 8]
for idx, element in enumerate(elements_to_insert):
    if idx == 0:
        root = TreeNode(element)
    else:
        insert(element, root)

# Print the greatest value
print(f"find_greatest_value : {find_greatest_value(root)}")

print("Printing all the Binary Search Tree elements")
print("inorder")
traverse_and_print_inorder(root)
print("preorder")
traverse_and_print_preorder(root)
print("postorder")
traverse_and_print_postorder(root)

# Fill the Binary Search Tree
elements_to_insert = ["Moby Dick", "Great Expectations", "Robinson Crusoe", "Alice in Wonderland", "Lord of the Flies", "Pride and Prejudice", "The Odyssey"]
for idx, element in enumerate(elements_to_insert):
    if idx == 0:
        root_books = TreeNode(element)
    else:
        insert(element, root_books)

print("preorder root_books\n")
traverse_and_print_preorder(root_books)

# preorder root_books
#
# Moby Dick
# Great Expectations
# Alice in Wonderland
# Lord of the Flies
# Robinson Crusoe
# Pride and Prejudice
# The Odyssey

print("\n")

print("postorder root_books\n")
traverse_and_print_postorder(root_books)

# postorder root_books
#
# Alice in Wonderland
# Lord of the Flies
# Great Expectations
# Pride and Prejudice
# The Odyssey
# Robinson Crusoe
# Moby Dick