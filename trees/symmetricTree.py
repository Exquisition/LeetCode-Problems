# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        return self.check(root.left, root.right)
        
    def check(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        a = self.check(left.left, right.right)
        b = self.check(left.right, right.left)
        return a and b
        