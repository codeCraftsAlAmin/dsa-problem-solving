# Write a function findMissing(arr) that finds the missing number in an array of integers from 1 to n.
# Example: findMissing([1, 2, 4, 5, 6]) → 3
# ============================================
# Problem: Array
# Interview: #11
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Find Missing Number.
# Input: findMissing([1, 2, 4, 5, 6])
# Output: (3)
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# ============================================


numbers = [1, 2, 4, 5, 6]


# # solution: 1 == good
def findMissing_v1(numbers):

    n = max(numbers)

    for num in range(1, n + 1):
        if num not in numbers:
            return num


print(findMissing_v1(numbers))


# ============================================
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================


# # solution: 2 == better or mathematical formula
def findMissing_v2(numbers):
    n = max(numbers)

    return n * (n + 1) // 2 - sum(numbers)


print(findMissing_v2(numbers))
