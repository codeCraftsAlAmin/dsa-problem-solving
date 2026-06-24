# ============================================
# Problem: Array
# Interview: #8
# Difficulty: Medium
# ============================================
#
# Problem Statement:
# Flatten Nested Array.
# Input: flattenArray([1, [2, 3], [4, 5], 6])
# Output: ([1, 2, 3, 4, 5, 6])
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================

arr = [1, [2, 3], [4, 5], 6]


def flattenArray(arr):
    store = []
    for num in arr:
        if isinstance(num, list):
            store.extend(num)
        else:
            store.append(num)

    return store


print(flattenArray(arr))
