def bubble_sort(list1):
    """
    In Big Oh! worst case is quadratic O(N^2)
    """
    last_idx = len(list1) - 1
    swap = True

    while swap:
        swap = False
        for idx in range(last_idx):
            if list1[idx] > list1[idx + 1]:
                list1[idx], list1[idx + 1] = list1[idx + 1], list1[idx]
                swap = True

    return list1




def selection_sort(list1):
    """
    In Big Oh! worst case is quadratic O(N^2)
    Altough in reality, it is slower than bubble_sort
    since there is only 1 swap action per iteration
    """
    pass

test = bubble_sort([2, 6, 8, 9, 1])
print(test)

test = bubble_sort([9, 8, 7, 6, 5])
print(test)