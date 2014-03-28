# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def sort_to_BST(self, head, size):
        if head is None or size == 0:
            return None
        
        if size & 1:
            node_index = size / 2 + 1
            left_size = right_size = size / 2
        else:
            node_index = size / 2
            left_size = size / 2 - 1
            right_size = size / 2

	print size, node_index, left_size, right_size
        p = head
        for i in range(1, node_index):
            p = p.next

	print p.val
        node = TreeNode(p.val)
        node.left = self.sort_to_BST(head, left_size)
        node.right = self.sort_to_BST(p.next, right_size)
        
        return node
        
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None:
            return None
        
        if head.next is None:
            root = TreeNode(head.val)
            return root
        
        p = head
        size = 0
        while p:
            size += 1
            p = p.next

        root = self.sort_to_BST(head, size)
        return root

if __name__ == "__main__":
    l = [-1,0,1,2]
    print l
    head = ListNode(l[0])
    p = head
    for i in range(1, len(l)):
	node = ListNode(l[i])
        p.next = node
        p = p.next
    p.next = None

    s = Solution()
    root = s.sortedListToBST(head)

