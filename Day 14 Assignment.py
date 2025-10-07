# Remove common characters and concatenate
# Difficulty: BasicAccuracy: 30.78%Submissions: 79K+Points: 1Average Time: 30m
# Given two strings, s1 and s2. The task is to remove all characters that are common in both strings and then combine the remaining characters from each string to form a new string. The characters that are not shared between the two strings should appear in the result in the same order as they appear in their respective original strings. If, after removing the common characters, no characters are left to form the result, return "-1"

# Examples:

# Input: s1 = aacdb, s2 = gafd
# Output: cbgf
# Explanation: The common characters of s1 and s2 are: a, d. The uncommon characters of s1 and s2 are c, b, g and f. Thus the modified string with uncommon characters concatenated is cbgf.
# Input: s1 = abcs, s2 = cxzca
# Output: bsxz
# Explanation: The common characters of s1 and s2 are: a,c. The uncommon characters of s1 and s2 are b,s,x and z. Thus the modified string with uncommon characters concatenated is bsxz.

def concatenatedString(s1,s2):
        #code here
        final=''
        for item in s1:
            if item not in s2:
                final+=item
        for item in s2:
            if item not in s1:
                final+=item
        if len(final)==0:
            return -1
        else:
            return final
print(concatenatedString('aacdb','gafd'))