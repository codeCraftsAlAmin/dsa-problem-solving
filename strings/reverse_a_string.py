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


# # solution: 1 -- good
def reversedStr_v1(str):
    result = ""
    for i in range(len(str) - 1, -1, -1):
        result += str[i]
    return result


print(reversedStr_v1("olleh"))


# # solution: 2 -- better
def reversedStr_v2(str):
    result = []
    for i in range(len(str) - 1, -1, -1):
        result.append(str[i])
    return "".join(result)


print(reversedStr_v2("olleh"))


# ============================================
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================


# # solution: 3 -- best
def reversedStr_v3(str):
    return str[::-1]


print(reversedStr_v3("olleh"))
