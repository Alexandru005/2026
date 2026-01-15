# You are given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

# My solution
def minSubArrayLen(target, nums):
    min_length = len(nums)
    arrayLength = len(nums)
    contor = 0
    for i in range(len(nums)):
        j = i
        suma = 0
        length = 0
        while j < arrayLength and suma < target:
            suma += nums[j]
            length += 1
            j += 1
        if suma >= target:
            min_length = min(min_length, length)
            contor += 1

    if contor == 0:
        return 0
    else:
        return min_length

print(minSubArrayLen(10, [2,1,5,1,5,3]))







