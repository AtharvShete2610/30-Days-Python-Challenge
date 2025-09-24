# Given an array arr[] of positive integers. The task is to return the count of the number of odd and even elements in the array.

# Note: Return two elements where the first one in the count of odd & second one is the count of even.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: 3 2
# Explanation: There are 3 odd elements (1, 3, 5) and 2 even elements (2 and 4).

arr = list(map(int,input().split()))
def count(arr):
    even = 0
    odd = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd,even

print("Odd and Even Count is : ",count(arr))