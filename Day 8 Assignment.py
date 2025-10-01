# Reverse a String
# Difficulty: BasicAccuracy: 69.49%Submissions: 430K+Points: 1Average Time: 15m
# You are given a string s, and your task is to reverse the string.

# Examples:

# Input: s = "Geeks"
# Output: "skeeG"
# Input: s = "for"
# Output: "rof"
# Input: s = "a"
# Output: "a"

def revStr(s:str):
    return s[::-1]
print(revStr("GeeksforGeeks"))