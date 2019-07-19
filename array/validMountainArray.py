class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        if len(A) < 3:
            return False
        
        n = len(A)
        
        incr_end = 0
        for i in range(1, n):
            if A[i] >= A[i-1]:
                incr_end += 1
            
        if incr_end == n-1 or incr_end == 0:
            return False
        
        
        
        for j in range(incr_end+1, n):
            if A[j] >= A[j-1]:
                return False
            
        
        return True
            
        