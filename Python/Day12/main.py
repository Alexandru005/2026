# You are given an integer array people where people[i] is the weight of the ith person,
# and an infinite number of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time,
# provided the sum of the weight of those people is at most limit.
#
# Return the minimum number of boats to carry every given person.

# My solution
def numRescueBoats(people, limit):
    people.sort()
    number_of_boats, l, r = 0, 0, len(people) - 1
    while l <= r:
        remain = limit - people[r]
        r -= 1
        number_of_boats += 1
        if l <= r and remain >= people[l]:
            l += 1
    return number_of_boats

print(numRescueBoats([5,1,2,4], 6))

# You are given an integer array nums and an integer k,
# return true if there are two distinct indices i and j
# in the array such that nums[i] == nums[j] and abs(i - j) <= k,
# otherwise return false.

# My solution
def containsNearbyDuplicate(nums, k):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if abs(i - j) <= k and nums[i] == nums[j]:
                return True
    return False

print(containsNearbyDuplicate([2,1,2], 1))


# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#
# Return the maximum profit you can achieve. You may choose to not make any transactions,
# in which case the profit would be 0.


# My solution
def maxProfit(prices):
    max_profit = 0
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
    return max_profit

print(maxProfit([7,1,5,3,6,4]))














