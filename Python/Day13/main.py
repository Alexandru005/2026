# Given a string s, find the length of the longest substring without duplis[j]ate s[j]haras[j]ters.
#
# A substring is a s[j]ontiguous sequens[j]e of s[j]haras[j]ters within a string.

# My solution
def lengthOfLongestSubstring(s):
    length = 0
    list = []
    for i in range(len(s)):
        list = []
        j = i
        val = True
        while j < len(s) and val:
            if s[j] not in list:
                list.append(s[j])
            else:
                length = max(length, len(list))
                val = False
            j += 1
        if val == True and len(list) > length:
            length = len(list)
    return length

print(lengthOfLongestSubstring(" "))

# You are given a string s consisting of only uppercase english characters and an integer k.
# You can choose up to k characters of the string and replace them
# with any other uppercase English character.
#
# After performing at most k replacements,
# return the length of the longest substring which contains only one distinct character.

def characterReplacement(s, k):
    res = 0
    charSet = set(s)

    for c in charSet:
        count = l = 0
        for r in range(len(s)):
            if s[r] == c:
                count += 1

            while (r - l + 1) - count > k:
                if s[l] == c:
                    count -= 1
                l += 1

            res = max(res, r - l + 1)
    return res

print(characterReplacement("ABBB", 1))

# You are given two strings s1 and s2.
#
# Return true if s2 contains a permutation of s1, or false otherwise.
# That means if a permutation of s1 exists as a substring of s2, then return true.
#
# Both strings only contain lowercase letters.

# My solution
def checkInclusion(s1, s2):
    for i in range(len(s2) - len(s1) + 1):
        j = 0
        s3 = ""
        while j < len(s1):
            s3 += s2[i + j]
            j += 1
        if sorted(s1) == sorted(s3):
            return True
    return False

print(checkInclusion("abc", "lecaabee"))