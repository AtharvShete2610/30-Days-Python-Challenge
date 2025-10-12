# Second Largest
# Difficulty: EasyAccuracy: 26.72%Submissions: 1.4MPoints: 2Average Time: 15m
# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.

def secondLargest(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1,len(arr)):
            if arr[max_index] > arr[j]:
                continue
            else:
                max_index = j
        arr[i],arr[max_index] = arr[max_index],arr[i]

        if i > 0:
            return arr[i]
    return -1
print(secondLargest([12, 35, 1, 10, 34, 1]))