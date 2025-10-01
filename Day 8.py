# Reverse a String
# Difficulty: BasicAccuracy: 70.82%Submissions: 91K+Points: 1
# Given a string s , return reverse of the string as output.

# Example 1:

# Input: 
# s = "GeeksforGeeks"
# Output: "skeeGrofskeeG" 
# Explanation: Reverse string of "GeeksforGeeks" will be "skeeGrofskeeG"
# Example 2:

# Input: 
# s = "ReversE"
# Output: "EsreveR"
# Explanation: Reverse string of "ReversE" will be "EsreveR"

def revStr(s:str):
    res = ''
    for i in range(len(s)-1,-1,-1):
        res += s[i]
    return res
print(revStr("GeeksforGeeks"))