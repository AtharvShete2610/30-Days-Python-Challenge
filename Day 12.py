# Upper Case Conversion
# Difficulty: BasicAccuracy: 38.13%Submissions: 51K+Points: 1
# Given a string s, convert the first letter of each word in the string to uppercase. 

# Examples:

# Input: s = "gEEKs"
# Output: "GEEKs"
# Input: s = "i love programming"
# Output: "I Love Programming"

def convert(s):
    # Method 1
    # new_s = s.split(' ')
    # for i in range(len(new_s)):
    #     word = new_s[i]
    #     word_up = word[0].upper()
    #     new_word = word_up + word[1:]
    #     new_s[i] = new_word
    # final_s = ' '.join(new_s)
    # return final_s

    # Method 2
    new_s = ''
    flag = True
    for char in s:
        if flag == True:
            new_s += char.upper()
            flag = False
        else:
            if char == " ":
                new_s += char
                flag = True
            else:
                new_s += char
    return new_s
print(convert("i love programming"))