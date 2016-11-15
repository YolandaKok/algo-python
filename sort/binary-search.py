"""
    ----------------------------
    Binary Search implementation
    ----------------------------
    return (True or False if the key item is into the array)
"""
import math

def binarySearch(a, key):
    # left border of the subarray
    left = 1
    # right border of the subarray
    right = len(a)
    while right >= left:
        i = int(math.floor((left + right) / 2))
        if a[i] == key:
            return True
        elif a[i] > key:
            right = i - 1
        elif a[i] < key:
            left = i + 1
    return False

# test
a = [1 , 3, 8, 15, 19, 31]
key = 19
print binarySearch(a, key)
