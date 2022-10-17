"""
Chapter 14 - Node-Based Data Structures
"""
import stacks_queues as sq

class Node:
    """
    A Node holds data
    and the pointer to the next Node
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

class LinkedList:
    def __init__(self, first_node):
        """
        Pass the 1st Node of the LinkedList
        """
        self.first_node = first_node

    def read(self, index):
        """
        Read from the LinkedList
        Just like an array, the first index is number 0
        """
        # We begin at the first node of the list:
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            # We keep following the links of each node until we get to the
            # index we're looking for:
            current_node = current_node.next_node
            current_index += 1

            # If we're past the end of the list, that means the
            # value cannot be found in the list, so return None:
            if not current_node:
                return None
            
        return current_node.data

    def index_of(self, value):
        """
        Look up for the index based on the value provided
        """
        # We begin at the first node of the list:
        current_node = self.first_node
        current_index = 0

        while current_node:
            # If we find the data we're looking for, we return it:
            if current_node.data == value:
                return current_index

            # Otherwise, we move on the next node:
            current_node = current_node.next_node
            current_index += 1

        # If we get through the entire list without finding the
        # data, we return None:
        return None

    def insert_at_index(self, index, value):
        """
        """
        # We create the new node with the provided value:
        new_node = Node(value)

        # If we are inserting at the beginning of the list:
        if index == 0:
            # Have our new node link to what was the first node:
            new_node.next_node = self.first_node
            # Establish that the our new node is now the list's first node:
            self.first_node = new_node
            return

        # If we are inserting anywhere other than the beginning:

        current_node = self.first_node
        current_index = 0

        # First, we access the node immediately before where the
        # new node will go:
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1

        # Have the new node link to the next node:
        new_node.next_node = current_node.next_node

        # Modify the link of the previous node to point to
        # our new node:
        current_node.next_node = new_node

    def delete_at_index(self, index):
        """
        """
        # If we are deleting the first node:
        if index == 0:
            # Simply set the first node to be what is currently the second node:
            self.first_node = self.first_node.next_node
            return

        current_node = self.first_node
        current_index = 0

        # First, we find the node immediately before the one we
        # want to delete and call it current_node:
        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1

        # We find the node that comes after the one we're deleting: 
        node_after_deleted_node = current_node.next_node.next_node

        # We change the link of the current_node to point to the
        # node_after_deleted_node, leaving the node we want
        # to delete out of the list:
        current_node.next_node = node_after_deleted_node

    def print_all_elements(self):
        """
        Print all elements in the list
        """
        current_node = self.first_node
        current_index = 1

        while current_node:
            print(f"Node #{current_index} : {current_node.data}")
            current_node = current_node.next_node
            current_index += 1

    def return_last_element(self):
        """
        Returns the last element from the list
        """
        current_node = self.first_node

        while current_node.next_node:
            current_node = current_node.next_node

        return current_node.data

    def reverse_linked_list(self):
        """
        Reverses the list. That is, if the original list is A -> B -> C,
        all of the list's links should change so that C -> B -> A.
        """
        # Instantiate a Stack
        stack = sq.Stack()

        # Push all Nodes into the Stack
        current_node = self.first_node

        while current_node:
            stack.push(current_node)
            current_node = current_node.next_node

        # Pop node by node from the Stack and link them
        node_from_stack = stack.pop()
        self.first_node = node_from_stack

        while len(stack):
            next_node_from_stack = stack.pop()
            node_from_stack.next_node = next_node_from_stack
            node_from_stack = next_node_from_stack

        # Last node in the Linked List should point to None
        node_from_stack.next_node = None

    def delete_middle_node(self, node):
        """
        delete based on node
        """
        node.data = node.next_node.data
        node.next_node = node.next_node.next_node

class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, value):
        """
        Inserts to the last of the DoublyLinkedList
        """
        new_node = Node(value)

        # If there are no elements yet in the linked list:
        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        # If the linked list already has at least one node:
        else:
            # New Node's previous should be pointing to the last element in the DoublyLinkedList
            new_node.previous_node = self.last_node
            # also, this former last Node should be using as next the New Node
            self.last_node.next_node = new_node
            # Finally the New Node is becoming the last element in the DoublyLinkedList
            self.last_node = new_node

    def remove_from_front(self):
        """
        Removes from the front  of the DoublyLinkedList
        """
        # Identify the first Node
        removed_node = self.first_node
        # The new first Node is the 2nd Node so we point to it
        self.first_node = self.first_node.next_node
        # The former first Node is returned
        return removed_node


    def print_elements_in_reverse(self):
        """
        prints all the elements of the list in reverse order.
        """
        current_node = self.last_node

        while current_node:
            print(f"Node : {current_node.data}")
            current_node = current_node.previous_node