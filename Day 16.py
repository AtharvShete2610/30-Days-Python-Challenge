# First Occurence
# Difficulty: BasicAccuracy: 46.9%Submissions: 212K+Points: 1Average Time: 20m
# Given two strings txt and pat, return the 0-based index of the first occurrence of the substring pat in txt. If pat is not found, return -1.
# Note: You are not allowed to use the inbuilt function.

# Examples :

# Input: txt = "GeeksForGeeks", pat = "Fr"
# Output: -1
# Explanation: "Fr" is not present in the string "GeeksForGeeks" as substring.
# Input: txt = "GeeksForGeeks", pat = "For"
# Output: 5
# Explanation: "For" is present as substring in "GeeksForGeeks" from index 5 (0 based indexing).
# Input: txt = "GeeksForGeeks", pat = "gr"
# Output: -1
# Explanation: "gr" is not present in the string "GeeksForGeeks" as substring.

def firstOccurence(txt,pat):
    for i in range(len(txt)):
        val = txt[i]
        val2 = pat[0]
        if val2 == val:
            search = txt[i:i+len(pat)]
            if search == pat:
                return i
            else:
                continue
        else:
            continue
    return -1
print(firstOccurence('GeeksForGeeks','Fr'))