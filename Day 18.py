# Remove vowels from string
# Difficulty: BasicAccuracy: 41.92%Submissions: 52K+Points: 1
# Given a string s. Your task is to remove the vowels from the string.

# Examples:

# Input: s = "welcome to geeksforgeeks"
# Output: "wlcm t gksfrgks"
# Explanation: Vowels were ignored only consonents were returned in the same order.
# Input: s = "what is your name ?"
# Output: wht s yr nm ?

def removeVowels(s):
    res = ''
    vowel = 'aeiouAEIOU'
    for char in s:
        if char in vowel:
            continue
        else:
            res += char
    return res
print(removeVowels('welcome to geeksforgeeks'))