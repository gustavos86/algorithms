"""
Tests for file linkedlist.py
"""
from linkedlist import *

def test_read():
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")

    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4

    linked_list = LinkedList(node_1)

    test = linked_list.read(0)
    result = "once"
    assert test == result

    test = linked_list.read(1)
    result = "upon"
    assert test == result

    test = linked_list.read(2)
    result = "a"
    assert test == result

    test = linked_list.read(3)
    result = "time"
    assert test == result

def test_index_of():
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")

    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4

    linked_list = LinkedList(node_1)

    test = linked_list.index_of("once")
    result = 0
    assert test == result

    test = linked_list.index_of("upon")
    result = 1
    assert test == result

    test = linked_list.index_of("a")
    result = 2
    assert test == result

    test = linked_list.index_of("time")
    result = 3
    assert test == result

def test_insert_at_index():
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")

    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4

    linked_list = LinkedList(node_1)

    linked_list.insert_at_index(3, "great")

    test = linked_list.index_of("time")
    result = 4
    assert test == result

def test_delete_at_index():
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")
    node_5 = Node("in")
    node_6 = Node("Seattle")

    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4
    node_4.next_node = node_5
    node_5.next_node = node_6

    linked_list = LinkedList(node_1)

    linked_list.delete_at_index(0)

    test = linked_list.read(0)
    result = "upon"
    assert test == result

    linked_list.delete_at_index(2)

    test = linked_list.read(2)
    result = "in"
    assert test == result

def test_print_all_elements(capfd):
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")
    node_5 = Node("in")
    node_6 = Node("Seattle")

    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4
    node_4.next_node = node_5
    node_5.next_node = node_6

    linked_list = LinkedList(node_1)

    result = ""
    result += f"Node #1 : once\n"
    result += f"Node #2 : upon\n"
    result += f"Node #3 : a\n"
    result += f"Node #4 : time\n"
    result += f"Node #5 : in\n"
    result += f"Node #6 : Seattle\n"

    linked_list.print_all_elements()
    out, err = capfd.readouterr()
    assert out == result

def test_return_last_element():
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")
    node_5 = Node("in")
    node_6 = Node("Seattle")

    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4
    node_4.next_node = node_5
    node_5.next_node = node_6

    linked_list = LinkedList(node_1)

    test = linked_list.return_last_element()
    result = "Seattle"
    assert test == result

def test_reverse_linked_list(capfd):
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")

    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4

    linked_list = LinkedList(node_1)

    result = ""
    result += f"Node #1 : time\n"
    result += f"Node #2 : a\n"
    result += f"Node #3 : upon\n"
    result += f"Node #4 : once\n"

    linked_list.reverse_linked_list()

    linked_list.print_all_elements()
    out, err = capfd.readouterr()
    assert out == result

def test_delete_middle_node(capfd):
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")
    node_5 = Node("in")
    node_6 = Node("Seattle")

    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4
    node_4.next_node = node_5
    node_5.next_node = node_6

    linked_list = LinkedList(node_1)

    linked_list.delete_middle_node(node_3)
    result = ""
    result += f"Node #1 : once\n"
    result += f"Node #2 : upon\n"
    result += f"Node #3 : time\n"
    result += f"Node #4 : in\n"
    result += f"Node #5 : Seattle\n"

    linked_list.print_all_elements()
    out, err = capfd.readouterr()
    assert out == result

    linked_list.delete_middle_node(node_5)
    result = ""
    result += f"Node #1 : once\n"
    result += f"Node #2 : upon\n"
    result += f"Node #3 : time\n"
    result += f"Node #4 : Seattle\n"

    linked_list.print_all_elements()
    out, err = capfd.readouterr()
    assert out == result

def test_DoublyLinkedList(capfd):
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")

    node_1.next_node = node_2

    node_2.previous_node = node_1
    node_2.next_node     = node_3

    node_3.previous_node = node_2
    node_3.next_node     = node_4

    node_4.previous_node = node_3

    doubly_linked_list = DoublyLinkedList(node_1, node_4)

    result = ""
    result += f"Node : time\n"
    result += f"Node : a\n"
    result += f"Node : upon\n"
    result += f"Node : once\n"

    doubly_linked_list.print_elements_in_reverse()
    out, err = capfd.readouterr()
    assert out == result