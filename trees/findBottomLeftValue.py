# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # return first node in the last level of level order traversal
        
        q = collections.deque([root])
        
        while q:            
            nodes = []
            
            for _ in range(len(q)):
                # all the nodes in q represent the current level
                node = q.popleft()
                nodes.append(node)
            
                if node.left:
                    q.append(node.left)
                          
                if node.right:
                    q.append(node.right)
                

        return nodes[0].val
        