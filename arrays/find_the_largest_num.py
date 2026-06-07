# ============================================
# Problem: Array
# Interview: #2
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Find the Largest Number.
# Input: findMax([3, 7, 2, 9, 1])
# Output: (9)
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================

# # solution: 1
arr = [3, 7, 2, 9, 11]


def maxNumber(arr):
    max = arr[0]
    for num in arr:
        if max < num:
            max = num
    return max


print(maxNumber(arr))

# ============================================
# Problem: Array
# Interview: #2
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Find the Largest Number.
# Input: findMax([3, 7, 2, 9, 1])
# Output: (9)
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================

# # solution: 2
arr = [3, 7, 2, 19, 11]


def findMax(arr):
    return max(arr)


print(maxNumber(arr))
