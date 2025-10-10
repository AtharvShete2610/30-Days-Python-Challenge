# Count of smaller elements
# Difficulty: BasicAccuracy: 54.54%Submissions: 121K+Points: 1Average Time: 20m
# Given an unsorted array arr. Find the count of elements less than or equal to the given element x.

# Examples:

# Input: x = 9, arr = [10, 1, 2, 8, 4, 5] 
# Output: 5
# Explanation: The 5 elements are 1, 2, 8, 4 and 5.
# Input: x = 2, arr = [1, 2, 2, 5, 7, 2, 9] 
# Output: 4 
# Explanation: The 4 elements are 1, 2, 2 and 2.

def smaller_ele(x,arr):
    count = 0
    for i in arr:
        if i <= x:
            count += 1
        else:
            continue
    return count
print(smaller_ele(9,[10, 1, 2, 8, 4, 5] ))