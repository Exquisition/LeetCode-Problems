# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if (p and not q) or (not p and q):
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
        