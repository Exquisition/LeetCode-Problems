# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        
        two pointers slow and fast
        if they meet together at some point, there is a cycle
        if they never meet and we reach the end of the linked list, there is no cycle
        """
    
        
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow and fast and fast.next:
            
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next
            
        return False
            
        
        