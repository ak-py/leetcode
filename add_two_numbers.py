"""
URL = https://leetcode.com/problems/add-two-numbers/

Finished in about 10-15 mins. Missed an edge case. Was too eager to submit.
Solved the question with two extra variables. Soltuion was not in top 50%.
Looked at my previous submissions. Realized the better solution without those extra variables.
Coded it and submitted. Now in top 10% solutions.

REDO - Long Term

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = curr = ListNode(0)

        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry = carry // 10

        return dummy.next
