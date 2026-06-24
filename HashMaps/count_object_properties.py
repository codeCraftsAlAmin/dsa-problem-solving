# ============================================
# Problem: HashMap
# Interview: #20
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Count Object Properties.
# Input: {a: 1, b: 2, c: 3}
# Output: 3
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================


input = {"a": 1, "b": 2, "c": 3}


def countProperties(obj):
    count = 0

    for key in obj:
        count += 1
    return count


print(countProperties(input))
