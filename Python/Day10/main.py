# You are given an integer array nums sorted in non-decreasing order.
# Your task is to remove duplicates from nums in-place so that each element appears only once.
#
# After removing the duplicates, return the number of unique elements,
# denoted as k, such that the first k elements of nums contain the unique elements.
#
# Note:
#
# The order of the unique elements should remain the same as in the original array.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain all the unique elements.
# Return k as the final result.

# My solution
def removeDuplicates(nums):
    k = 0
    nums.sort()
    prev = nums[0]
    lista = []

    if nums == []:
        return k

    for i in range(1, len(nums)):
        if nums[i] != prev:
            k = k + 1
            lista.append(prev)
            prev = nums[i]

    k = k + 1
    lista.append(prev)

    for i in range(0, len(lista)):
        nums[i] = lista[i]

    return k

print(removeDuplicates([1,1,2,3,4]))

# Given an array of integers numbers that is sorted in non-decreasing order.
#
# Return the indices (1-indexed) of two numbers, [index1, index2],
# such that they add up to a given target number target and index1 < index2.
# Note that index1 and index2 cannot be equal,
# therefore you may not use the same element twice.
#
# There will always be exactly one valid solution.

# My solution
def twoSum(numbers, target):
    index1 = -1
    index2 = -1

    for i in range(0,len(numbers)):
        if (target - numbers[i]) in numbers and  index1 == -1:
            index1 = i + 1
        if index1 != -1 and (target - numbers[index1 - 1]) == numbers[i]:
            index2 = i + 1

    return [index1, index2]

print(twoSum([2,3,4], 6))


#You are given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# My solution
def rotate(nums, k):
    lista = [0] * len(nums)
    for i in range(0, len(nums)):
        if i + k < len(nums):
            lista[i+k] = nums[i]
        else:
            index = (i + k) % len(nums)
            lista[index] = nums[i]

    for i in range(0, len(nums)):
        nums[i] = lista[i]

print(rotate([1,2,3,4,5], 7))









