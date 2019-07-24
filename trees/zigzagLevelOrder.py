# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # use a direction flag to flip level list every other level
         
        if root is None:
            return []
        
        queue = [root]
        ans = []
        
        direction = 1
        
        while queue:
            level = []
            
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
          
            if direction == -1:
                ans.append(level[::-1])
            else:
                ans.append(level)
                
            direction *= -1
            
        return ans
        