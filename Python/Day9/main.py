# You are given a string s, return true if the s can be a palindrome
# after deleting at most one character from it.

# My solution
def validPalindrome(s):
    def palindrome(s):
        return s == s[::-1]
    for i in range(len(s)):
        new_s = s[0 : i] + s[i + 1 : len(s)]
        if palindrome(new_s):
            return True
    return False

print(validPalindrome("abd"))
print(validPalindrome("abca"))

# You are given two strings, word1 and word2.
# Construct a new string by merging them in alternating order,
# starting with word1 — take one character from word1,
# then one from word2, and repeat this process.

# My solution
def mergeAlternately(word1, word2):
    i = 0
    new_string = ""
    min_len = min(len(word1), len(word2))
    while i < min_len:
        new_string += word1[i] + word2[i]
        i += 1
    if i < len(word1):
        new_string += word1[i:]
    if i < len(word2):
        new_string += word2[i:]
    return new_string

print(mergeAlternately("", "abcd"))
print(mergeAlternately("abc", "abcd"))
print(mergeAlternately("abcd", "abc"))

# You are given two integer arrays nums1 and nums2,
# both sorted in non-decreasing order, along with two integers m and n, where:
#
# m is the number of valid elements in nums1,
# n is the number of elements in nums2.
# The array nums1 has a total length of (m+n),
# with the first m elements containing the values to be merged,
# and the last n elements set to 0 as placeholders.
#
# Your task is to merge the two arrays
# such that the final merged array is also sorted in non-decreasing order
# and stored entirely within nums1.
# You must modify nums1 in-place and do not return anything from the function.

# My solution
def merge(nums1, m, nums2, n):
    new_list = []
    indexm = 0
    indexn = 0
    while m > 0 and n > 0:
        if nums1[indexm] < nums2[indexn]:
            new_list.append(nums1[indexm])
            indexm += 1
            m -= 1
        else:
            new_list.append(nums2[indexn])
            indexn += 1
            n -= 1
    while m > 0:
        new_list.append(nums1[indexm])
        m -= 1
        indexm += 1
    while n > 0:
        new_list.append(nums2[indexn])
        n -= 1
        indexn += 1
    for i in range(0, len(nums1)):
        nums1[i] = new_list[i]

merge([0,0],2,[1,2],2)



















