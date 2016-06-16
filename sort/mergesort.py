# Mergesort Algorithm

def Mergesort(a, l, r):
    # if there is not only one element in the list
    if l < r:
<<<<<<< HEAD
        
=======
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
    left = [0] * capacity1
    right = [0] * capacity2

    # copy the elements of list a to the subarrays
    for i in range(0, capacity1):
        left[i] = a[l + i]

    for j in range(0, capacity2):
        right[j] = a[q + 1 + j]

    # indexes for arrays
    i = 0
    j = 0
    k = l

    while i < capacity1 and j < capacity2:
        # choice of the first element in list a
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    # if list one has not ended
    while i < capacity1:
        a[k] = left[i]
        i +=1
        k += 1

    while j < capacity2:
        a[k] = right[j]
        j += 1
        k += 1


a = [2, 1, 10, 9]
Mergesort(a, 0, 3)

for i in range(0, 4):
    print a[i]
>>>>>>> feature
