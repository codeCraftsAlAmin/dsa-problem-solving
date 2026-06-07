# ============================================
# Problem: Array
# Interview: #3
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Find the Largest Number.
# Input: secondLargest([3, 7, 2, 9, 1])
# Output: (7)
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================

list = [3, 7, 2, 9, 1]


def largestNum(list):
    largest = list[0]
    second_largest = list[1]

    for num in list:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest < num:
            second_largest = num

    return second_largest


print(largestNum(list))
