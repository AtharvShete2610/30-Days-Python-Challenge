# Repeated Character
# Difficulty: BasicAccuracy: 43.15%Submissions: 88K+Points: 1
# Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

# NOTE - If there are no repeating characters return '#'.

# Example 1:

# Input:
# S = "geeksforgeeks"
# Output: g
# Explanation: g, e, k and s are the repeating
# characters. Out of these, g occurs first. 
# Example 2:

# Input: 
# S = "abcde"
# Output: -1
# Explanation: No repeating character present. (You need to return '#')

def repeatedChar(s):
    # out = {}
    # for char in s:
    #     if char in out:
    #         out[char] += 1
    #     else:
    #         out[char] = 1
    # for key,value in out.items():
    #     if value > 1:
    #         return key
    #     else:
    #         continue
    # return '#'

    for i in range(len(s)):
        val = s[i]
        for j in range(1,len(s)):
            val1 = s[j]
            if val == val1:
                return val
            else:
                continue
        return '#'
print(repeatedChar('geeksforgeeks'))