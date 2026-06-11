# ============================================
# Problem: Array
# Interview: #9
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Capitalize Each Word.
# Input: capitalizeWords("hello world from js")
# Output: ("Hello World From Js")
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================

words = "hello world from js"


# # solution: 1 -- good
def capitalizeWords_v1(words):
    splitWords = words.split()
    result = []

    for word in splitWords:
        capitalize = word[0].upper() + word[1:].lower()
        result.append(capitalize)

    return " ".join(result)


print(capitalizeWords_v1(words))

# ============================================
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================


# # solution: 2 -- best
def capitalizeWords_v2(words):
    return words.title()


print(capitalizeWords_v2(words))
