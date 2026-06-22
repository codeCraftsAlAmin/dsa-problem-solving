# Problem 10: Count Occurrences of a Character  [Easy]
# Description: Write a function countChar(str, char) that returns how many times a character appears in a string.
# Example:
# Input: 'banana', 'a'  → Output: 3
# Hint: Use split(char).length - 1 or a loop.

# ============================================
# Problem: String
# Interview: #18
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Count Occurrences of a Character.
# Input: 'banana', 'a'
# Output: (3)
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# ============================================

text = "banana"


# # solution: 1 == good
def countChar_v1(str, char):
    count = 0
    for i in str:
        if i == char:
            count += 1
    return count


print(countChar_v1(text, "a"))


# # solution: 1 == better
def countChar_v2(str, char):
    return str.count(char)


print(countChar_v2(text, "a"))
