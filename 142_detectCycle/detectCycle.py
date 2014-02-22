'''
Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        p = head
        q = head
        while p and q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                i = 1
                j = 0
		# count the nodes in the loop
		# start from 1 and p == q, should p.next here
                while p.next != q:
                    p = p.next
                    i += 1
		# find the number i node from head
                p = head
                for j in range(i):
                    p = p.next
		# one from head and another one from number i node move at the same pace
                q = head
                while q != p:
                    p = p.next
                    q = q.next
                return p
        return None
