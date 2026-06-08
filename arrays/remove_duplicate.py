# ============================================
# Problem: Array
# Interview: #7
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Remove Duplicates from Array.
# Input: removeDuplicates([1, 2, 2, 3, 4, 4, 5])
# Output: ([1, 2, 3, 4, 5])
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# ============================================


arr = [1, 2, 2, 3, 4, 4, 5]


# # solution: 1 -- good
def removeDuplicates_v1(arr):

    items = []

    for num in arr:
        if num not in items:
            items.append(num)
    return items


print(removeDuplicates_v1(arr))


# ============================================
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================


# # solution: 1 -- best
def removeDuplicates_v2(arr):
    return list(set(arr))


print(removeDuplicates_v2(arr))
