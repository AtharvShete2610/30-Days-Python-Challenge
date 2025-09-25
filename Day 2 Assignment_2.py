# Given two strings  S1 and S2 . You have to concatenate both the strings and print the concatenated string.

# Example 1:

# Input:
# S1 = "Geeksfor"
# S2 = "Geeks"
# Output: GeeksforGeeks
# Explanation: Combined "Geeksfor" and "Geeks"
 

# Example 2:

# Input:
# S1 = "Practice"
# S2 = "Hard"
# Output: PracticeHard
# Explanation: Combined "Practice" and "Hard"

def concat_str(s1,s2):
    return s1 + s2
print(concat_str('abcd','efgh'))