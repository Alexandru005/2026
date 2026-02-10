# Implement a last-in-first-out (LIFO) stack using only two queues.
# The implemented stack should support
# all the functions of a normal stack (push, top, pop, and empty).
#
# Implement the MyStack class:
#
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.

# My solution
class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.insert(0, x)

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
#
# Implement the MyQueue class:
#
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# My solution
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


# Design a stack class that supports the push, pop, top, and getMin operations.
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# My solution
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



