# Given an integer array nums and an integer k,
# return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# My solution
def topKFrequent(nums, k):
    nums.sort()
    list = []
    count = 0
    prev = nums[0]
    rez = []
    for num in nums:
        if num == prev:
            count += 1
        else:
            list.append((count, prev))
            prev = num
            count = 1
    list.append((count, prev))
    list.sort(reverse=True)
    for i in range(k):
        rez.append(list[i][1])
    return rez

# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.

# My solution
def productExceptSelf(nums):
    list = [1] * len(nums)

    for i in range (len(nums)):
        for j in range(len(nums)):
            if i != j:
                list[i] = list[i] * nums[j]

    return list

# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
# The elements do not have to be consecutive in the original array.

# My solution
def longestConsecutive(nums):
    if nums == []:
        return 0
    multime = set()
    for num in nums:
        multime.add(num)
    list = []
    for num in multime:
        list.append(num)
    list.sort()
    seq = 1
    rez = 0
    for i in range(len(list)-1):
        if list[i] == list[i+1] - 1:
            seq += 1
        else:
            if(rez < seq):
                rez = seq
            seq = 1
    if rez < seq:
        rez = seq
    return rez






