# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock.
# However, you can buy it then immediately sell it on the same day.
# Also, you are allowed to perform any number of transactions but can hold at most one share of the stock at any time.
# Find and return the maximum profit you can achieve.

# My solution
def maxProfit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += (prices[i] - prices[i - 1])

    return profit

# You are given an integer array nums of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# You can return the result in any order.

# My solution
def majorityElement(nums):
    nums.sort()
    n = len(nums)
    list = []
    prev = nums[0]
    count = 0

    for num in nums:
        if num == prev:
            count += 1
        else:
            if count > n // 3:
                list.append(prev)
            count = 1
            prev = num
    if count > n // 3:
        list.append(prev)

    return list

# You are given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# My solution
def subarraySum(nums, k):
    sol = 0
    for i in range(len(nums)):
        sum = nums[i]
        if sum == k:
            sol += 1
        for j in range(i + 1, len(nums)):
            sum += nums[j]
            if sum == k:
                sol += 1
    return sol














