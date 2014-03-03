'''
Reorder List
Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # for print usage
    def __repr__(self):
	p = self
	st = "{"
	while p:
	    if p.next is not None:
		st += str(p.val) + ", "
	    else:
		st += str(p.val)
	    p = p.next
	st += "}"
        return st

class Solution:
    # Recursive method won't pass the large test case
    def reverseList1(self, head):
        if head is None or head.next is None:
            return head
        p = head.next
        q = self.reverseList(p)
        p.next = head
        head.next = None
        return q

    # Use 3 pointers will be accept by OJ
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None:
            return

	# Calculate the length of the list
        i = 0
        p = head
        while p:
            i += 1
            p = p.next

	# Find the tail node of the first half
        if i & 1 == 0:
            j = i / 2
        else:
            j = i / 2 + 1
        q = head
        while q and j > 1:
            j -= 1
            q = q.next

	# Reverse the last half and set tail node next for None
        t = self.reverseList(q.next)
        q.next = None

	# Reorder the list as request
        p = head
        while p and t:
            x = p.next
            p.next = t
            y = t.next
            t.next = x
            p = x
            t = y

        return

# Test case for debugging
def createList(data):
   size = len(data)
   if size == 0:
        return None

   head = ListNode(data[0])
   p = head
   for i in range(1, size):
	q = ListNode(data[i])
        p.next = q
        p = q
   p.next = None
   return head

def main():
    data = [1, 2, 3, 4]
    head = createList(data)
    print head

    s = Solution()
    s.reorderList(head)
    print head

    data = [1, 2, 3, 4, 5, 6, 7]
    head = createList(data)
    print head

    s = Solution()
    s.reorderList(head)
    print head

if __name__ == "__main__":
    main()
