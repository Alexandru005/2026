# You are given an array of integers temperatures where temperatures[i]
# represents the daily temperatures on the ith day.
#
# Return an array result where result[i] is the number of days after the ith day
# before a warmer temperature appears on a future day.
# If there is no day in the future where a warmer temperature will appear for the ith day,
# set result[i] to 0 instead.

# My solution
def dailyTemperatures(temperatures):
    result = []
    def function(temp, val, res):
        if temp == []:
            return 0
        if temp[0] > val:
            return res
        if temp[0] <= val:
            return function(temp[1:], val, res + 1)
    for i in range(len(temperatures)):
        result.append(function(temperatures[i:], temperatures[i], 0))
    return result

print(dailyTemperatures([22,21,20]))


# You are given an array asteroids of integers representing asteroids in a row.
# The indices of the asteriod in the array represent their relative position in space.
#
# For each asteroid, the absolute value represents its size,
# and the sign represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet.

def asteroidCollision(asteroids):
    condition = True
    length = len(asteroids)
    while length > 1 and condition:
        condition = False
        for i in range(length - 1):
            if asteroids[i] > 0 and asteroids[i + 1] < 0:
                condition = True
                if abs(asteroids[i]) < abs(asteroids[i + 1]):
                    asteroids.pop(i)
                    length -= 1
                    break
                if abs(asteroids[i]) > abs(asteroids[i + 1]):
                    asteroids.pop(i + 1)
                    length -= 1
                    break
                if abs(asteroids[i]) == abs(asteroids[i + 1]):
                    asteroids.pop(i)
                    asteroids.pop(i)
                    length -= 2
                    break
    return asteroids

print(asteroidCollision([2,4,-4,-1]))

# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
#
# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.
#
# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:
#
# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.

# My solution
class StockSpanner:

    def __init__(self):
        self.lista =  []

    def next(self, price):
        count = 1
        for i in range(len(self.lista) - 1, -1, -1):
            if self.lista[i] <= price:
                count += 1
            else:
                break
        self.lista.append(price)
        return count