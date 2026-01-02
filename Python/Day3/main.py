# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements
# which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
import collections


# My Soulution
# def removeElement(nums, val):
#     lista = []
#     for num in nums:
#         if num != val:
#             lista.append(num)
#     for i in range(len(lista)):
#         nums[i] = lista[i]
#     return len(lista)



# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times in the array.
# You may assume that the majority element always exists in the array.

# My Solution
# def majorityElement(nums):
#     nums.sort()
#
#     rez = nums[0]
#     maxaperance = 1
#
#     count = 0
#     val = nums[0]
#
#     for i in range(0,len(nums)):
#         if nums[i] == val:
#             count += 1
#         if nums[i] != val:
#             if count > maxaperance:
#                 maxaperance = count
#                 rez = val
#             val = nums[i]
#             count = 1
#
#     if count > maxaperance:
#         rez = val
#
#     return rez

# Better option
# def majorityElement(nums):
#     nums.sort()
#     return nums[len(nums) // 2]


# You are given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
# and with the smallest space complexity possible.

# My Solution
# def sortArray(nums):
#     def quicksort(a, prim, ultim):
#         stanga = prim + 1
#         dreapta = ultim
#
#         mid = (prim + ultim) // 2
#         a[prim], a[mid] = a[mid], a[prim]
#         pivot = a[prim]
#
#         while stanga <= dreapta:
#             while stanga <= ultim and a[stanga] < pivot:
#                 stanga += 1
#             while dreapta >= prim and a[dreapta] > pivot:
#                 dreapta -= 1
#             if stanga < dreapta:
#                 a[stanga], a[dreapta] = a[dreapta], a[stanga]
#                 stanga += 1
#                 dreapta -= 1
#             else:
#                 stanga += 1
#
#         a[prim], a[dreapta] = a[dreapta], a[prim]
#
#         if prim < dreapta - 1:
#             quicksort(a, prim, dreapta - 1)
#         if dreapta + 1 < ultim:
#             quicksort(a, dreapta + 1, ultim)
#
#     quicksort(nums, 0, len(nums) - 1)
#     return nums


# def sortArray(nums):
#     nums.sort()
#     return nums