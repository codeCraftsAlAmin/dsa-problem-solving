# ============================================
# Problem: Array
# Interview: #6
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Sum of Array.
# Input: sumArray([1, 2, 3, 4, 5])
# Output: (15)
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================
from functools import reduce

arr = [1, 2, 3, 4, 5]


# # solution: 1 == good
def sumArray(arr):
    return reduce(lambda x, y: x + y, arr)


print(sumArray(arr))


# # solution: 1 == better
def sumArray_v2(arr):
    sum = 0

    for num in arr:
        sum += num

    return sum


print(sumArray_v2(arr))


# # solution: 3 == best
def sumArray(arr):
    return sum(arr)


print(sumArray(arr))
