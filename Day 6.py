# Check if a string is Isogram or not
# Difficulty: EasyAccuracy: 63.25%Submissions: 66K+Points: 2Average Time: 30m
# Given a string s of lowercase alphabets, You have to check that  it is isogram or not.
# An Isogram is a string in which no letter occurs more than once.

# Examples:

# Input: s = "machine"
# Output: true
# Explanation: "machine" is an isogram as no letter has appeared twice. so we return true.
# Input: s = "geeks"
# Output: false
# Explanation: "geeks" is not an isogram as 'e' appears twice. so we return false.

# def isIsogram(s):
#     res = {}
#     for char in s:
#         if char in res:
#             return False
#         else:
#             res[char] = 1
#     return True


def isIsogram(s):
    for i in range(len(s)):
        val = s[i]
        for j in range(i+1,len(s)):
            val2 = s[j]
            if val == val2:
                return False
            else:
                continue
    return True
print(isIsogram('machine'))