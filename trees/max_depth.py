# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        depth = 0
        q = []
        
        q.append(root)
        
        
        while q:
            
            depth += 1
            
            level_size = len(q)
            
            for i in range(level_size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        
        return depth
            
            