# Count of camel case characters
# Difficulty: BasicAccuracy: 71.16%Submissions: 33K+Points: 1
# Given a string. Count the number of Camel Case characters in it.

# Example 1:

# Input:
# S = "ckjkUUYII"
# Output: 5
# Explanation: Camel Case characters present:
# U, U, Y, I and I.

# â€‹Example 2:

# Input: 
# S = "abcd"
# Output: 0
# Explanation: No Camel Case character
# present.

def count_camel_case(s):
    camel_case = 0
    for i in s:
        if i.isupper():
            camel_case += 1
    return camel_case

print(count_camel_case("ckjkUUYII"))