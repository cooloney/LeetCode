# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorder(self, root, res):
        if root is None:
            return

        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        res = []
        self.preorder(root, res)
        return res
