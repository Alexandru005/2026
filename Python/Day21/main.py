# You are given a non-negative integer x, return the square root of x rounded
# down to the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
from operator import truediv


# My solution
# def mySqrt(x):
#     val = 0
#     if x == 0 or x == 1:
#         return x
#     for i in range(0,x//2 + 1):
#         if i * i <= x:
#             if i * i == x:
#                 return i
#             else:
#                 val = i
#     return val

def mySqrt(x):
    def binary_search(val, res, start, end):
        if start < end:
            mid = (start + end) // 2
            if mid * mid == val:
                return mid
            elif mid * mid > val:
                return binary_search(val, res, start, mid - 1)
            else:
                return binary_search(val, mid, mid + 1, end)
        else:
            if start * start <= val and start > res:
                return start
            elif end * end <= val and end > res:
                return end
            return res
    return binary_search(x, 0, 0, x)

for i in range(1, 10):
    print(str(i) + " " + str(mySqrt(i)))

# You are given an m x n 2-D integer array matrix and an integer target.
#
# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.
#
# Can you write a solution that runs in O(log(m * n)) time?

# My solution
def searchMatrix(matrix, target):
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
    def binary_search_matrix(matrix, target, st, dr):
        if st <= dr:
            mid = (st + dr) // 2
            if matrix[mid][0] <= target and matrix[mid][len(matrix[mid]) - 1] >= target:
                return binarySearch(matrix[mid], target, 0, len(matrix[mid]))
            elif matrix[mid][0] > target:
                return binary_search_matrix(matrix, target, st, mid - 1)
            elif matrix[mid][len(matrix[mid]) - 1] < target:
                return binary_search_matrix(matrix, target, mid + 1, dr)
        else:
            return False
    return binary_search_matrix(matrix, target, 0, len(matrix) - 1)

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


# You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
# You are also given an integer h, which represents the number of hours you have to eat all the bananas.
#
# You may decide your bananas-per-hour eating rate of k.
# Each hour, you may choose a pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, you may finish eating the pile
# but you can not eat from another pile in the same hour.
#
# Return the minimum integer k such that you can eat all the bananas within h hours.

# My solution
def minEatingSpeed(piles, h):
    piles.sort()
    def solution(nums, val, h):
        sum = 0
        for i in range(len(nums)):
            if nums[i] % val == 0:
                sum += nums[i] // val
            else:
                sum += nums[i] // val + 1
        if sum <= h:
            return 1
        return -1
    def binarySearch(nums, target, st, dr):
        if st <= dr:
            mid = (st + dr) // 2
            if solution(nums, mid, target) == 1:
                res = binarySearch(nums, target, st, mid - 1)
                if res != None:
                    return min(mid, res)
                else:
                    return mid
            else:
                return binarySearch(nums, target, mid + 1, dr)
    return binarySearch(piles, h, 1, piles[len(piles) - 1])

print(minEatingSpeed([3,6,7,11], 8))





