# Given the beginning of a singly linked list head, reverse the list,
# and return the new beginning of the list.

def reverseList(head):
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
#
# The new list should be made up of nodes from list1 and list2.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    rez = l = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            l.next = list1
            list1 = list1.next
        else:
            l.next = list2
            list2 = list2.next
        l = l.next

    l.next = list1 or list2

    return rez.next

