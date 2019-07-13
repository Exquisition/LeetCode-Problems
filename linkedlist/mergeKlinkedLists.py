# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq as hq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        h = []
        
        numElements = 0
        
        for l in lists:
            while l:
                numElements += 1
                hq.heappush(h, l.val)
                l = l.next
                
        dummy = ListNode(0)
        curr = dummy
        
        for i in range(numElements):
            curr.next = ListNode(hq.heappop(h))
            curr = curr.next
            
        return dummy.next
            
        
        
       
        