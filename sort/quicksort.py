# Quicksort implementation

# definition of the partition subroutine

def partition(a, l, r):
    # pivot first element of the array
    pivot = a[l]
    index = l
    for i in range(l + 1, r):
        if a[i] <= pivot:
            index += 1
            # tuple packing instead of swap function
            a[i], a[index] = a[index], a[i]
    a[index], a[l] = a[l], a[index]
    return index

def quicksort(a, l, r):
    if l < r:
        q = partition(a, l, r)
        quicksort(a, l, q - 1)
        quicksort(a, q + 1, r)

b = [4, 3, 5, 7, 2]
i = 0
quicksort(b, i, len(b) - 1)
for j in range(i, len(b) - 1):
    print b[j]
