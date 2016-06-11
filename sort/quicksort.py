# Quicksort implementation

# definition of the partition subroutine

def swap(a, b):
    temp = a
    a = b
    b = temp

def partition(a, l, r):
    # pivot first element of the array
    pivot = a[l]
    index = l
    for i in range(l + 1, r):
        if a[i] <= pivot:
            index+= 1
            swap(a[i], a[index])
    swap(pivot, a[index])
    return index

def quicksort(a, l, r):
    q = partition(a, l, r)
    quicksort(a, l, q - 1)
    quicksort(a, q + 1, r)

b = [4, 3, 5, 7]
i = 0
quicksort(b, i, len(b) - 1)
for j in range(i, len(b) - 1):
    print b[j],
