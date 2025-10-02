# Palindrome Array
# Difficulty: BasicAccuracy: 43.54%Submissions: 79K+Points: 1
# Given an array arr, the task is to find whether the arr is palindrome or not. If the arr is palindrome then return true else return false.

# An array is said to be palindrome if its reverse array matches the original array. 

# Examples:

# Input: arr = [1, 2, 3, 2, 1]
# Output: true
# Explanation: Here we can see we have [1, 2, 3, 2, 1] if we reverse it we can find [1, 2, 3, 2, 1] which is the same as before. So, the answer is true.
# Input: arr = [1, 2, 3, 4, 5]
# Output: false
# Explanation: Here we can see we have [1, 2, 3, 4, 5] if we reverse it we find [5, 4, 3, 2, 1] which is the not same as before. So, the answer false.

import copy
def isPalindrome(arr):
    if arr[::] == arr[::-1]:
        return True
    else:
        return False

    # arr1 = copy.deepcopy(arr)
    # i = 0
    # j = len(arr1) - 1
    # while i < j:
    #     arr1[i],arr1[j] == arr1[j],arr1[i]
    #     i += 1
    #     j -= 1
    #     if arr1 == arr:
    #         return True
    #     else:
    #         return False

print(isPalindrome([1,2,3,2,1]))
