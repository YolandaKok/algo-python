"""
    ------------------------
    Quicksort implementation
    ------------------------
    Worst case complexity: O(n^2)
    pseudo code: Introduction to Algorithms 3rd edition

"""

def partition(a, l, r):
    """ Pivot is the first element of the list."""
    pivot = a[l]
    index = l
    for i in range(l + 1, r + 1):
        if a[i] <= pivot:
            index += 1
            # tuple packing instead of swap function
            a[i], a[index] = a[index], a[i]
    a[l], a[index] = a[index], a[l]
    return index

def quicksort(a, l, r):
    """
        Input: list a, l-> left index, r-> right index
        Output: ascending sequence of elements
    """
    if l < r:
        q = partition(a, l, r)
        quicksort(a, l, q - 1)
        quicksort(a, q + 1, r)
