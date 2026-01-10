# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#
# The output should not contain any duplicate triplets.
# You may return the output and the triplets in any order.

# My solution
def threeSum(nums):
    res = set()
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp = [nums[i], nums[j], nums[k]]
                    res.add(tuple(tmp))
    return [list(i) for i in res]


print(threeSum([0,0,0,0]))

# You are given an integer array nums of size n,
# return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
# such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# My solution
def fourSum(nums, target):
    nums.sort()
    res = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                for n in range(k + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] + nums[n] == target:
                        tmp = [nums[i], nums[j], nums[k], nums[n]]
                        res.add(tuple(tmp))
    return [list(i) for i in res]


print(fourSum([3,2,3,-3,1,0], 3))


# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

# My solution
def maxArea(height):
    max_area = 0
    for i in range(len(height) - 1):
        for j in range(i+1, len(height)):
            area = min(height[i], height[j]) * (j - i)
            if area > max_area:
                max_area = area
    return max_area

print(maxArea([1,7,2,5,4,7,3,6]))






