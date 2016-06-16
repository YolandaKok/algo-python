# Mergesort Algorithm

def Mergesort(a, l, r):
    # if there is not only one element in the list
    if l < r:
        q = (l + r) / 2
        # first half
        Mergesort(a, l, q)
        # second half
        Mergesort(a, q + 1, r)
        Merge(a, l, q, r)

def Merge(a, l, q, r):
    # bound for the first temporary array
    capacity1 = q - l + 1
    # bound for the second temporary array
    capacity2 = r - q
    # initialize the temporary arrays
    for i in range(0, capacity1):
        left[i] = 0

    for j in range(0, capacity2):
        right[j] = 0

    # copy the elements of list a to the subarrays
            
