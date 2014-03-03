# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self, root, res):
        if root is None:
            return

        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)

    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        res = []
        self.postorder(root, res)
        return res
