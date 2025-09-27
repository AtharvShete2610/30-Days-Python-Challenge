# Count type of Characters
# Difficulty: BasicAccuracy: 59.65%Submissions: 30K+Points: 1
# Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.
# Note: There are no white spaces in the string.

# Example 1:

# Input:
# S = "#GeeKs01fOr@gEEks07"
# Output:
# 5
# 8
# 4
# 2
# Explanation: There are 5 uppercase characters,
# 8 lowercase characters, 4 numeric characters
# and 2 special characters.

# Example 2:

# Input: 
# S = "*GeEkS4GeEkS*"
# Output:
# 6
# 4
# 1
# 2
# Explanation: There are 6 uppercase characters,
# 4 lowercase characters, 1 numeric characters
# and 2 special characters.

def count(s):
    upper_count = 0
    lower_count = 0
    numeric = 0
    spe_char = 0

    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
        elif i.isalnum():
            numeric += 1
        else:
            spe_char += 1
    return upper_count,lower_count,numeric,spe_char

print(count("#GeeKs01fOr@gEEks07"))