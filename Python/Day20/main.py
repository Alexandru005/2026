# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
#
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
#
# Your solution must run in
# O(logn) time.

# My solution
def search(nums, target):
    def binary_search(nums, target, st, dr):
        if st <= dr:
            mid = (st + dr) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(nums, target, mid + 1, dr)
            return binary_search(nums, target, st, mid - 1)
        else:
            return -1
    return binary_search(nums, target, 0, len(nums) - 1)

print(search([-1,0,3,5,9,12], 13))

# You are given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

# My solution
def searchInsert(nums, target):
    def binary_search(nums, target, st, dr):
        if st <= dr:
            mid = (st + dr) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(nums, target, mid + 1, dr)
            return binary_search(nums, target, st, mid - 1)
        else:
            return dr + 1
    return binary_search(nums, target, 0, len(nums) - 1)

print(searchInsert( [-1,0,2,4,6,8], 13))


# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I will tell you whether
# the number I picked is higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns three possible results:
#
# 0: your guess is equal to the number I picked (i.e. num == pick).
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# Return the number that I picked.

# My solution
def guessNumber(n):
    l, r = 1, n
    while True:
        m = (l + r) // 2
        res = guess(m)
        if res > 0:
            l = m + 1
        elif res < 0:
            r = m - 1
        else:
            return m