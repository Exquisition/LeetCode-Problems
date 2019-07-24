# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        if not head.next:
            return head
        
        curr = head
        nextNode = head.next
        
        while curr and nextNode:
         
            curr_value = curr.val
            next_value = nextNode.val
            
            if curr_value == next_value:
                curr.next = nextNode.next
                nextNode = nextNode.next
            else: 
                curr = curr.next
                nextNode = nextNode.next
        
        return head
            
        