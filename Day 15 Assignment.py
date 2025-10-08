# Alternates in an Array
# Difficulty: BasicAccuracy: 52.74%Submissions: 217K+Points: 1Average Time: 15m
# You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).

# Examples:

# Input: arr[] = [1, 2, 3, 4]
# Output: 1 3
# Explanation:
# Take first element: 1
# Skip second element: 2
# Take third element: 3
# Skip fourth element: 4
# Input: arr[] = [1, 2, 3, 4, 5]
# Output: 1 3 5
# Explanation:
# Take first element: 1
# Skip second element: 2
# Take third element: 3
# Skip fourth element: 4
# Take fifth element: 5

def alternate(arr):
    out = []
    for i in range(len(arr)):
        if i % 2 == 0:
            out.append(arr[i])
        else:
            continue
    return out
print(alternate([1, 2, 3, 4]))