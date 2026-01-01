# Given an array of integers nums and an integer target,
# return the indices i and j such that
# nums[i] + nums[j] == target and i != j.

#My solution
# def twoSum(nums, target):
#     for i in range(len(nums) - 1):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]



# You are given an array of strings strs.
# Return the longest common prefix of all the strings.
# If there is no longest common prefix, return an empty string "".

# My Solution
# def longestCommonPrefix(strs):
#     pref = ""
#     strs.sort()
#     i = 0
#     for s in strs[0]:
#         for j in range(1, len(strs)):
#             if s != strs[j][i]:
#                 return pref
#         pref += s
#         i += 1
#     return pref



# Given an array of strings strs, group all anagrams together into sublists.
# You may return the output in any order.

# My Solution
# def groupAnagrams(strs):
#     list = []
#     for i in range (len(strs)):
#         ok = 0
#         for j in range (len(list)):
#             if sorted(strs[i]) == sorted(list[j][0]):
#                 list[j].append(strs[i])
#                 ok = 1
#         if ok == 0:
#             list.append([strs[i]])
#     return list

