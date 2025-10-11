# Remove Spaces
# Difficulty: BasicAccuracy: 49.21%Submissions: 81K+Points: 1
# Given a string s. Your task is to remove spaces from it. 

# Examples:

# Input: s = "geeks  for geeks"
# Output: "geeksforgeeks"
# Explanation: All the spaces have been removed.
# Input: s = "    g f g"
# Output: "gfg"
# Explanation: All the spaces including the leading ones have been removed.

def removeSpaces(s):
    res = ''
    for i in s:
        if i == ' ':
            continue
        else:
            res += i
    return res
print(removeSpaces('geeks  for geeks'))