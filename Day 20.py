# Binary String
# Difficulty: BasicAccuracy: 53.99%Submissions: 84K+Points: 1Average Time: 20m
# Given a binary string s. You have to count the number of substrings that start and end with 1.

# Examples:

# Input: s = "1111"
# Output: 6
# Explanation: There are 6 substrings from the given string. They are "11", "11", "11", "111", "111", "1111".
# Input: s = "01101"
# Output: 3
# Explanation: There are 3 substrings from the given string. They are "11", "101", "1101".

def binarySubstring(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
    return (count*(count-1)) // 2
print(binarySubstring("1111"))