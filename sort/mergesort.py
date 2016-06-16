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
