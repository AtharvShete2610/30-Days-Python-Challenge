# One odd Occuring
# Difficulty: BasicAccuracy: 50.53%Submissions: 90K+Points: 1
# Given an array of arr[] positive integers where all numbers occur even number of times except one number which occurs odd number of times. Return that number.

# Examples:

# Input:arr[] = [1, 2, 3, 2, 3, 1, 3]
# Output: 3
# Explaination: 3 occurs three times.
# Input:arr[] = [5, 7, 2, 7, 5, 2, 5]
# Output: 5
# Explaination: 5 occurs three times.

def Odd(arr):
    res = {}
    for i in arr:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    for key,value in res.items():
        if value % 2 != 0:
            return key
    return -1
print(Odd([5, 7, 2, 7, 5, 2, 5]))