# Convert a list of characters into a String
# Difficulty: BasicAccuracy: 63.69%Submissions: 31K+Points: 1
# Given a list of characters, merge all of them into a string.

# Example 1:

# Input:
# N = 13
# Char array = g e e k s f o r g e e k s
# Output: geeksforgeeks 
# Explanation: combined all the characters
# to form a single string.

# Example 2:

# Input:
# N = 4
# Char array = e e b a
# Output: eeba
# Explanation: combined all the characters
# to form a single string.

def convert(n,arr):
    res=['' if i==' ' else i for i in arr]
    return ''.join(res)

print(convert(13,'g e e k s f o r g e e k s'))