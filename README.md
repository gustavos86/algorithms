# algorithms

![Alt text](/book_cover/book_cover.jpg "Optional title")

## pytest

Every commit should show include an output of the tests passing.

```
S C:\Users\gusta\projects\algorithms> pytest -v   
==================================================================================== test session starts ====================================================================================
platform win32 -- Python 3.10.5, pytest-7.1.3, pluggy-1.0.0 -- C:\Users\gusta\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\gusta\projects\algorithms
collected 21 items

test_ch13.py::test_exercise01 PASSED                                                                                                                                                   [  4%] 
test_ch13.py::test_exercise02 PASSED                                                                                                                                                   [  9%] 
test_ch13.py::test_exercise03 PASSED                                                                                                                                                   [ 14%] 
test_dynamic_programming.py::test_add_until_100 PASSED                                                                                                                                 [ 19%] 
test_dynamic_programming.py::test_golomb PASSED                                                                                                                                        [ 23%] 
test_dynamic_programming.py::test_unique_paths PASSED                                                                                                                                  [ 28%] 
test_linkedlist.py::test_read PASSED                                                                                                                                                   [ 33%] 
test_linkedlist.py::test_index_of PASSED                                                                                                                                               [ 38%] 
test_linkedlist.py::test_insert_at_index PASSED                                                                                                                                        [ 42%] 
test_linkedlist.py::test_delete_at_index PASSED                                                                                                                                        [ 47%] 
test_linkedlist.py::test_print_all_elements PASSED                                                                                                                                     [ 52%]
test_linkedlist.py::test_return_last_element PASSED                                                                                                                                    [ 57%] 
test_linkedlist.py::test_reverse_linked_list PASSED                                                                                                                                    [ 61%] 
test_linkedlist.py::test_delete_middle_node PASSED                                                                                                                                     [ 66%] 
test_linkedlist.py::test_DoublyLinkedList PASSED                                                                                                                                       [ 71%] 
test_recursion.py::test_traverse_array PASSED                                                                                                                                          [ 76%] 
test_recursion.py::test_ch11_exercise1 PASSED                                                                                                                                          [ 80%] 
test_recursion.py::test_ch11_exercise2 PASSED                                                                                                                                          [ 85%] 
test_recursion.py::test_ch11_exercise3 PASSED                                                                                                                                          [ 90%] 
test_recursion.py::test_ch11_exercise4 PASSED                                                                                                                                          [ 95%] 
test_sorting_algorithms.py::test_all_sorting_algorithms PASSED                                                                                                                         [100%]

==================================================================================== 21 passed in 0.20s ===================================================================================== 
PS C:\Users\gusta\projects\algorithms>
```