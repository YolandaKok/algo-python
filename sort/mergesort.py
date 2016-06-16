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
    
