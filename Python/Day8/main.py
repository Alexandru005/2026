# You are given an unsorted integer array nums.
# Return the smallest positive integer that is not present in nums.

# My solution
def firstMissingPositive(nums):
    sol = 1
    nums.sort()
    for num in nums:
        if num == sol:
            sol += 1
    return sol




# You are given an array of characters which represents a string s.
# Write a function which reverses a string

# My solution
def reverseString(s):
    for i in range(len(s) // 2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]



# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward.
# It is also case-insensitive and ignores all non-alphanumeric characters.

# My solution
def isPalindrome(s):
   s = s.lower()
   text = ""
   for c in s:
       if 'a' <= c <= 'z' or '0' <= c <= '9':
           text += c
   for i in range(len(text) // 2):
       if text[i] != text[len(text) - 1 - i]:
           return False
   return True

print(isPalindrome('Was it a car or a cat I saw?'))














