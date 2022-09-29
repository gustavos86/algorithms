"""
I am studying sorting algorithms along with their Big Oh notation
"""

def bubble_sort(list1):
    """
    In Big Oh! worst case is quadratic O(N^2)

    During each interation of the inner for loop,
    the largest value is moved to the right until
    it reaches the las index of the array.
    Next, the last index of the array gets decremented
    in order to not go that far again.
    """
    list1 = list1.copy()

    len_list1 = len(list1)
    swap = True

    while swap:
        swap = False
        len_list1 -= 1
        for idx in range(len_list1):
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
    list1 = list1.copy()

    idx = 0
    len_list1 = len(list1)

    for i in range(idx, len_list1):
        min_j = list1[i]
        j_idx = 0
        for j in range(idx + 1, len_list1):
            if list1[j] < min_j:
                min_j = list1[j]
                j_idx = j
        if j_idx:
            list1[i], list1[j_idx] = list1[j_idx], list1[i]
        idx += 1

    return list1

test = bubble_sort([2, 6, 8, 9, 1])
print(test)

test = bubble_sort([9, 8, 7, 6, 5])
print(test)

test = selection_sort([2, 6, 8, 9, 1])
print(test)

test = selection_sort([9, 8, 7, 6, 5])
print(test)