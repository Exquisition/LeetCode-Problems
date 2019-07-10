class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
		
		
		reverses a linked list between nodes m and n
        """
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(m - 1):
            prev = prev.next
        
        cur = prev.next
        post = cur.next
        
        for i in range(n - m):
            cur.next = post.next
            post.next = prev.next
            prev.next = post
            post = cur.next
        
        return dummy.next
		
		
