# algorithms

## pytest

Every commit should show include an output of the tests passing.

```
PS C:\Users\gusta\projects\algorithms> pytest -v
================================================================================= test session starts ==================================================================================
platform win32 -- Python 3.10.5, pytest-7.1.3, pluggy-1.0.0 -- C:\Users\gusta\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\gusta\projects\algorithms
collected 9 items

test_dynamic_programming.py::test_add_until_100 PASSED                                                                                                                            [ 11%] 
test_dynamic_programming.py::test_golomb PASSED                                                                                                                                   [ 22%] 
test_dynamic_programming.py::test_unique_paths PASSED                                                                                                                             [ 33%] 
test_recursion.py::test_traverse_array PASSED                                                                                                                                     [ 44%]
test_recursion.py::test_ch11_exercise1 PASSED                                                                                                                                     [ 55%] 
test_recursion.py::test_ch11_exercise2 PASSED                                                                                                                                     [ 66%] 
test_recursion.py::test_ch11_exercise3 PASSED                                                                                                                                     [ 77%] 
test_recursion.py::test_ch11_exercise4 PASSED                                                                                                                                     [ 88%] 
test_sorting_algorithms.py::test_all_sorting_algorithms PASSED                                                                                                                    [100%]

================================================================================== 9 passed in 0.05s =================================================================================== 
PS C:\Users\gusta\projects\algorithms> 
```