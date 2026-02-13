#You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
#
# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning.
# Rotating the array 6 times produces the original array.
#
# Assuming all elements in the rotated sorted array nums are unique,
# return the minimum element of this array.

# My solution
def findMin(nums):
    nums.sort()
    return nums[0]



# You are given an array of length n which was originally sorted in ascending order.
# It has now been rotated between 1 and n times.
# For example, the array nums = [1,2,3,4,5,6] might become:
#
# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.
#
# You may assume all elements in the sorted rotated array nums are unique,

# My solution
def search1(nums, target):
    def binarySearch(nums, target, st, dr):
        if st <= dr:
            mid = (st + dr) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binarySearch(nums, target, mid + 1, dr)
            return binarySearch(nums, target, st, mid - 1)
        else:
            return -1

    i = 0
    while i < len(nums) - 1:
        if nums[i] < nums[i + 1]:
            i += 1
        else:
            break
    if i != len(nums) - 1:
        a = binarySearch(nums, target, 0, i)
        b = binarySearch(nums, target, i + 1, len(nums) - 1)

        if a != -1:
            return a
        return b
    else:
        return binarySearch(nums, target, 0, len(nums) - 1)

print(search1([3], 4))

# You are given an array of length n which was originally sorted in non-decreasing
# order (not necessarily with distinct values). It has now been rotated between 1 and n times.
# For example, the array nums = [1,2,3,4,5,6] might become:
#
# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Given the rotated sorted array nums and an integer target,
# return true if target is in nums, or false if it is not present.

# My solution
def search(nums, target):
    def binarySearch(nums, target, st, dr):
        if st <= dr:
            mid = (st + dr) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                return binarySearch(nums, target, mid + 1, dr)
            return binarySearch(nums, target, st, mid - 1)
        else:
            return False

    i = 0
    while i < len(nums) - 1:
        if nums[i] <= nums[i + 1]:
            i += 1
        else:
            break
    if i != len(nums) - 1:
        a = binarySearch(nums, target, 0, i)
        b = binarySearch(nums, target, i + 1, len(nums) - 1)

        if a != False:
            return a
        return b
    else:
        return binarySearch(nums, target, 0, len(nums) - 1)