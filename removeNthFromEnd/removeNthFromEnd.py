# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p = head
        i = 0
        while i < n:
            p = p.next
            i = i + 1

        # Remove head
        if p is None:
            return head.next

        # Travel to the end
        q = r = head
        while p:
            p = p.next
            r = q
            q = q.next

        # Remove q
        r.next = q.next
        return head
