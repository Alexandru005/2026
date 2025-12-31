# You are given an integer array nums of length n.
# Create an array ans of length 2n where ans[i] == nums[i]
# and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

#My method
#O(n)
# def getConcatenation(self, nums):
#     n = len(nums)
#     ans = [0] * 2 * n
#     for i in range(n):
#         ans[i] = ans[i + n] = nums[i]
#     return ans

#The most efficient method
def getConcatenation(self, nums):
    ans = []
    for i in range(2):
        for num in nums:
            ans.append(num)
    return ans






# Given an integer array nums,
# return true if any value appears more than once
# in the array, otherwise return false.

#My method
#O(nlogn)
# def containsDuplicate(nums):
#     def binarysearch(nums, left, right, elem):
#         if left > right:
#             return False
#         mid = (left + right) // 2
#         if nums[mid] < elem:
#             return binarysearch(nums, mid + 1, right, elem)
#         elif nums[mid] > elem:
#             return binarysearch(nums, left, mid - 1, elem)
#         else:
#             return True
#
#     nums.sort()
#
#     for i in range(len(nums)):
#         a = binarysearch(nums, 0, i - 1, nums[i])
#         b = binarysearch(nums, i + 1, len(nums) - 1, nums[i])
#         if a or b :
#             return True
#     return False


# def hasDuplicate(nums):
#     nums.sort()
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i - 1]:
#             return True
#     return False

#The most efficient method
def hasDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False








# Given two strings s and t,
# return true if t is an anagram of s,
# and false otherwise.

# My solution
# O(1)
def isAnagram(s, t):
    return sorted(s) == sorted(t)

# The most efficent solution
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True