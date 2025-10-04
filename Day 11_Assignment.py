# Min and Max in Array
# Difficulty: BasicAccuracy: 68.55%Submissions: 382K+Points: 1Average Time: 10m
# Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

# Examples:

# Input: arr[] = [1, 4, 3, -5, -4, 8, 6]
# Output: [-5, 8]
# Explanation: minimum and maximum elements of array are -5 and 8.
# Input: arr[] = [12, 3, 15, 7, 9]
# Output: [3, 15]
# Explanation: minimum and maximum element of array are 3 and 15.

def minMax(arr):
    min = float('inf')
    max = float('-inf')
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
        else:
            continue
    return min,max

print(minMax([10, 20, 15, 2, 23, 90, 80]))