# You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).
# Input: arr[] = [1, 2, 3, 4]
# Output: 1 3
# Explanation:
# Take first element: 1
# Skip second element: 2
# Take third element: 3
# Skip fourth element: 4

arr = list(map(int,input().split()))
def alternate(arr):
    output = []
    for i in range(len(arr)):
        if i % 2 == 0:
            output.append(arr[i])
        else:
            continue
    return output

print(alternate(arr))
