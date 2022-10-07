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

def insertion_sort(list1):
    """
    1. In the first pass-through, we temporarily remove the value at index 1 (the second cell) and store it in a temporary variable.
    This will leave a gap at that index, since it contains no value.
    In subsequent pass-throughs, we remove the values at the subsequent indexes.

    2. We then begin a shifting phase, where we take each value to the left of the gap and compare it to the value in the temporary variable:
    If the value to the left of the gap is greater than the temporary variable, we shift that value to the right:
    As we shift values to the right, inherently the gap moves leftward. As soon as we encounter a value that is lower than the temporarily removed value, or we reach the left end of the array, this shifting phase is over.

    3. We then insert the temporarily removed value into the current gap.

    4. Steps 1 through 3 represent a single pass-through. We repeat these pass-throughs until the pass-through begins at the final index of the array. By then, the array will have been fully sorted.
    """
    list1 = list1.copy()

    len_list1 = len(list1)
    for i in range(1, len_list1):
        tmp = list1[i]

        c = i - 1
        while c > -1:
            if list1[c] > tmp:
                list1[c + 1] = list1[c]
                c -= 1
            else:
                break

        list1[c + 1] = tmp

    return list1

test = bubble_sort([2, 6, 8, 9, 1])
print(test)

test = bubble_sort([9, 8, 7, 6, 5])
print(test)

test = selection_sort([2, 6, 8, 9, 1])
print(test)

test = selection_sort([9, 8, 7, 6, 5])
print(test)

test = insertion_sort([2, 6, 8, 9, 1])
print(test)

test = insertion_sort([9, 8, 7, 6, 5])
print(test)