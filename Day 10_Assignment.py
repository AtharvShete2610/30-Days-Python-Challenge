# Non Repeating Character
# Difficulty: EasyAccuracy: 40.43%Submissions: 317K+Points: 2Average Time: 30m
# Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'.

# Examples:

# Input: s = "geeksforgeeks"
# Output: 'f'
# Explanation: In the given string, 'f' is the first character in the string which does not repeat.
# Input: s = "racecar"
# Output: 'e'
# Explanation: In the given string, 'e' is the only character in the string which does not repeat.
# Input: s = "aabbccc"
# Output: '$'
# Explanation: All the characters in the given string are repeating.

def nonrepeatChar(s):
    out = {}
    for char in s:
        if char in out:
            out[char] += 1
        else:
            out[char] = 1
    for key,value in out.items():
        if value == 1:
            return key
        else:
            continue
    return '$'
print(nonrepeatChar('geeksforgeeks'))