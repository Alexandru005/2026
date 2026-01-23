# You are given an array of integers nums and an integer k.
# There is a sliding window of size k that starts at the left edge of the array.
# The window slides one position to the right until it reaches the right edge of the array.
#
# Return a list that contains the maximum element in the window at each step.


#My solution
def maxSlidingWindow(nums, k):
    lista = []
    for i in range(len(nums) - k + 1):
        j = 0
        max = -10001
        while j < k:
            if nums[j+i] > max:
                max = nums[j+i]
            j += 1
        lista.append(max)
    return lista

print(maxSlidingWindow([1,2,1,0,4,2,6], 3))

