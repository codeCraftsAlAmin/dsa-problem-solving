# ============================================
# Problem: Logic
# Interview: #14
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Swap Two Variables.
# Input:  a = 5, b = 10
# Output: a = 10, b = 5
#
# Time Complexity:  O(1)
# Space Complexity: O(1)
# ============================================

a = 5
b = 10


# # solution: 1 == good
def swap_value_v1(a, b):
    temp = a
    a = b
    b = temp

    return a, b


print(swap_value_v1(a, b))


# #  solution: 2 == better
def swap_value_v2(a, b):
    a, b = b, a
    return a, b


print(swap_value_v2(a, b))
