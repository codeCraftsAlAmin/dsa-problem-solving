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


# # solution: 1 == good
def fibonacci(n):
    result = []
    a, b = 0, 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print(fibonacci(7))


# # solution: 2 == using recursion
def fibonacci_rec(n):

    if n == 0:
        return n
    elif n == 1:
        return n
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


print([fibonacci_rec(i) for i in range(7)])


# # Nth Fibonacci Number
def nthFib(n):

    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(nthFib(7))
