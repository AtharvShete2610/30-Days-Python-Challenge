# Given a string s, the task is to change the complete string to uppercase or lowercase depending on the case of the first character.

# Examples:

# Input: s = "abCD"
# Output: "abcd"
# Explanation: The first letter (a) is lowercase. Hence, the complete string is made lowercase.
# Input: s = "Abcd"
# Output: "ABCD"
# Explanation: The first letter (A) is uppercase. Hence, the complete string is made uppercase.

def str_convert(s):
    res = ''
    for i in range(len(s)):
        if s[0].islower():
            res = res + s.lower()
            break
        else:
            res = res + s.upper()
            break
    return res
print(str_convert('Abcd'))