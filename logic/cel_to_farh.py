# ============================================
# Problem: Math
# Interview: #16
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Celsius to Fahrenheit.
# Input: 0, 100
# Output: 32, 212
# Time Complexity: O(1)
# Space Complexity: O(1)
# ============================================


def toFahrenheit(celsius):

    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


print(toFahrenheit(100))
