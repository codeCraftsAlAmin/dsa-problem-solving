# ============================================
# Problem: HashMap
# Interview: #12
# Difficulty: Easy
# ============================================
#
# Problem Statement:
# Group By Property.
# Input: groupBy([{type:"fruit", name:"apple"}, {type:"veggie", name:"carrot"}, {type:"fruit", name:"mango"}], "type")
# Output: { fruit: [...], veggie: [...] }
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================


arr = [
    {"type": "fruit", "name": "apple"},
    {"type": "veggie", "name": "carrot"},
    {"type": "fruit", "name": "mango"},
]
key = "type"


# # solution: 1 == good
def groupBy_v1(arr, key):

    result = {}

    for item in arr:
        group = item[key]

        if group not in result:
            result[group] = []

        result[group].append(item)
    return result


print(groupBy_v1(arr, key))


# # solution: 2 == better
def groupBy_v2(arr, key):

    result = {}

    for item in arr:
        group = item[key]

        result.setdefault(group, []).append(item)
    return result


print(groupBy_v2(arr, key))
