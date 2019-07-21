# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inOrderWalk(self, root: TreeNode):
        
        if not root:
            return []
        
        if root.left: 
            self.inOrderWalk(root.left)
            
        self.inorderList.append(root.val)
        
        self.inOrderWalk(root.right)
        
        
            
            
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.inorderList = []
        
        self.inOrderWalk(root)
        
        print(self.inorderList)
        
        return self.inorderList[k-1]
        
            
        