import random
import sorting_algorithms as algo

def test_all_sorting_algorithms():
    test1 = [2, 6, 8, 1, 9, 1]
    solution1 = [1, 1, 2, 6, 8, 9]
    assert algo.bubble_sort(test1) == solution1
    assert algo.selection_sort(test1) == solution1
    assert algo.insertion_sort(test1) == solution1
    assert algo.quicksort(test1) == solution1

    test2 = [7, 9, 8, 7, 6, 5]
    solution2 = [5, 6, 7, 7, 8, 9]
    assert algo.bubble_sort(test2) == solution2
    assert algo.selection_sort(test2) == solution2
    assert algo.insertion_sort(test2) == solution2
    assert algo.quicksort(test2) == solution2

    solution3 = [x for x in range(1000)]
    test3 = solution3.copy()
    random.shuffle(test3)
    assert algo.bubble_sort(test3) == solution3
    assert algo.selection_sort(test3) == solution3
    assert algo.insertion_sort(test3) == solution3
    assert algo.quicksort(test3) == solution3
