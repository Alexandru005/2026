# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet.
# If key does not exist in the HashSet, do nothing.

# My solution
class MyHashSet:
    def __init__(self):
        self.data = set()

    def add(self, key):
        self.data.add(key)

    def remove(self, key):
        if self.contains(key):
            self.data.remove(key)

    def contains(self, key):
        return key in self.data


# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap.
# If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1
# if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value
# if the map contains the mapping for the key.

# My Solution
class MyHashMap:

    def __init__(self):
        self.data = dict()

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return -1

    def remove(self, key):
        if key in self.data:
            self.data.pop(key)



# You are given an array nums consisting of n elements where each element is an integer representing a color:
#
# 0 represents red
# 1 represents white
# 2 represents blue
# Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).
#
# You must not use any built-in sorting functions to solve this problem.
# My Solution
# O(n)
def sortColors(nums):
    list = [0] * 3

    for num in nums:
        list[num] += 1

    i = 0

    for j in range(3):
        while list[j]:
            nums[i] = j
            i += 1
            list[j] -= 1
