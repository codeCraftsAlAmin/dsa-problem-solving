# Problem 5: Check Positive, Negative or Zero  [Easy]
# Description: Write a function checkSign(n) that returns 'positive', 'negative', or 'zero' based on the value of n.
# Example:
# Input: -5  → Output: 'negative'Input: 0   → Output: 'zero'
# Hint: Use if-else if-else statements.

# ============================================
# Problem: Math
# Interview: #17
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Check Positive, Negative or Zero.
# Input: -5, 0
# Output: 'negative', 'zero'
# Time Complexity: O(1)
# Space Complexity: O(1)
# ============================================


def checkSign(n):
    if n == 0:
        return "zero"
    elif n > 0:
        return "positive"
    else:
        return "negative"


print(checkSign(0))
