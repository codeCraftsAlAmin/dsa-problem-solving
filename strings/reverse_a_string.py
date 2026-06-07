# ============================================
# Problem: Reverse String
# Interview: #1
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Write a function that reverses a string.
# Input: "hello"
# Output: "olleh"
#
# Time Complexity:  O(n^2), O(n)
# Space Complexity: O(n)
# ============================================


# # solution: 1
def reversedStr(str):
    result = ""
    for i in range(len(str) - 1, -1, -1):
        result += str[i]
    return result


print(reversedStr("olleh"))


# # solution: 2
def reversedStr(str):
    result = []
    for i in range(len(str) - 1, -1, -1):
        result.append(str[i])
    return "".join(result)


print(reversedStr("olleh"))


# ============================================
# Problem: Reverse String
# Interview: #1
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Write a function that reverses a string.
# Input: "hello"
# Output: "olleh"
#
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================


# # solution: 3
def reversedStr(str):
    return str[::-1]


print(reversedStr("olleh"))
