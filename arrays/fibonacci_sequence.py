# ============================================
# Problem: Array
# Interview: #10
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Fibonacci Sequence.
# Input: fibonacci(7)
# Output: [0, 1, 1, 2, 3, 5, 8]
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================


def fibonacci(n):
    result = []
    a, b = 0, 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print(fibonacci(7))
