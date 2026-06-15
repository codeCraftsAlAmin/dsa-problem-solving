# ============================================
# Problem: String
# Interview: #4
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Count Vowels.
# Input: countVowels("javascript")
# Output: (3)
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================

text = "javascript"


# # solution: 1 == good
def countVowels_v1(text):
    output = ""

    for i in range(len(text)):
        if (
            text[i] == "a"
            or text[i] == "e"
            or text[i] == "i"
            or text[i] == "o"
            or text[i] == "u"
        ):
            output += text[i]
    return len(output)


print(countVowels_v1(text))


# # solution: 2 == better
def countVowels_v2(text):
    count = 0
    for t in text:
        if t in "aeiou":
            count += 1
    return count


print(countVowels_v2(text))
