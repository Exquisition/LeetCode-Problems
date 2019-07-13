# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        
        first = dummy
        second = dummy
        
        for i in range(n+1):
            first = first.next

        while (first):
            first = first.next
            second = second.next
            
        second.next= second.next.next
        
        return dummy.next
        
        