'''
Insertion Sort List
Sort a linked list using insertion sort.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        p = self
        st = "{"
        while p:
            if p.next is None:
                st += str(p.val)
            else:
                st += str(p.val) + ", "
	    p = p.next
        st += "}"
        return st

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        new_head = None
        p = head
        while p:
            next = p.next
            if new_head is None or p.val < new_head.val:
                p.next = new_head
                new_head = p
            else:
                q = new_head
                while q:
                    if q.next is None or p.val < q.next.val:
                        p.next = q.next
                        q.next = p
                        break
                    q = q.next
            p = next
        return new_head


if __name__ == "__main__":
    head = ListNode(0)
    p = head
    for i in range(1, 5000):
        n = ListNode(i)
        p.next = n
	p = p.next
    print head

    s = Solution()
    p = s.insertionSortList(head)
    print p
