# ============================================
# Problem: Iteration
# Interview: #13
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# FizzBuzz.
# Input: fizzBuzz(15)
# Output: prints: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================
def fizzBuzz(n):
    for i in range(1, n + 1):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


fizzBuzz(15)
