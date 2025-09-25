# You are given an integer n. You need to convert all zeroes of n to 5.

# Examples:

# Input: n = 1004
# Output: 1554
# Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.
# Input: n = 121
# Output: 121
# Explanation: Since there are no zeroes in 121, the number remains as 121.

def convert(n):
    str_n = str(n)
    res = ''

    for char in str_n:
        if char == '0':
            res = res + '5'
        else:
            res += char
    return res
print(convert(1004))