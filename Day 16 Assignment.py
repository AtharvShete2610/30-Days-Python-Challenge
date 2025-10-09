# Print first letter of every word in the string
# Difficulty: BasicAccuracy: 71.6%Submissions: 49K+Points: 1
# Given a string S, the task is to create a string with the first letter of every word in the string.
 

# Example 1:

# Input: 
# S = "geeks for geeks"
# Output: gfg

# Example 2:

# Input: 
# S = "bad is good"
# Output: big

def firstAlphabate(S):
    res = S[0]
    for i in range(len(S)):
        if S[i] == ' ':
            res += S[i+1]
        else:
            continue
    return res
print(firstAlphabate('geeks for geeks'))