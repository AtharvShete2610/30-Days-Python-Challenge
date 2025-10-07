# Check for subsequence
# Difficulty: BasicAccuracy: 36.62%Submissions: 67K+Points: 1
# Given two strings A and B, find if A is a subsequence of B.

# Example 1:

# Input:
# A = AXY 
# B = YADXCP
# Output: 0 
# Explanation: A is not a subsequence of B
# as 'Y' appears before 'A'.
 

# Example 2:

# Input:
# A = gksrek
# B = geeksforgeeks
# Output: 1
# Explanation: A is a subsequence of B.

def isSubSequence(A, B):
        #code here
        count = 0
        start = 0
        for char in A:
            if start < len(B):
                for i in range(start,len(B)):
                    if B[i] == char:
                        count += 1
                        start = i + 1
                        break
                    else:
                        continue
        if count == len(A):
            return True
        else:
            return False
        
print(isSubSequence('AXY','YADXCP'))