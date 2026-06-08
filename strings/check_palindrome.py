# ============================================
# Problem: Reverse String
# Interview: #5
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Check Palindrome.
# Input: "racecar", "hello"
# Output: True, False
#
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================


text = "hello"


# # solution: 1 -- good
def isPalindrome_v1(text):
    p_text = ""
    for i in range(len(text) - 1, -1, -1):
        p_text += text[i]

    return p_text == text


print(isPalindrome_v1(text))


# ============================================
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================


# # solution: 1 -- better
def isPalindrome_v2(text):
    rev = text[::-1]

    return rev == text


print(isPalindrome_v2(text))
