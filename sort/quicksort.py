# Quicksort implementation

# definition of the partition subroutine

def partition(a, l, r):
    # pivot first element of the array
    pivot = a[l]
    index = l
    for i in range(l + 1, r:
        if a[i] <= pivot:
            index++
            swap(a[i], a[index])
    swap(a[pivot], a[index])
    return index

def quicksort(a, l, r):
    q = partition(a, l, r)
