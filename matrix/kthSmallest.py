import heapq as hq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        kth_smallest = matrix[0][0]
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        h = []
        
        for i in range(m):
            for j in range(n):
                hq.heappush(h, matrix[i][j])
                
        for i in range(k-1):
            hq.heappop(h)
            if i == k-2:
                kth_smallest = hq.heappop(h)
                
        return kth_smallest
                
        