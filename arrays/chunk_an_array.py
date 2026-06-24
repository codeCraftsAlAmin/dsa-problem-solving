# ============================================
# Problem: Array
# Interview: #19
# Difficulty: Medium
# ============================================
#
# Problem Statement:
# Chunk an Array.
# Input: [1,2,3,4,5], 2
# Output: [[1,2],[3,4],[5]]
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================

arr = [1, 2, 3, 4, 5]


def chunkArray(arr, size):
    result = []
    i = 0
    while i < len(arr):
        result.append(arr[i : i + size])
        i += size
    return result


print(chunkArray(arr, 2))
