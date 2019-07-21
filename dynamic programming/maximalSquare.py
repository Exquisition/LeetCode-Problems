class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if not matrix:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[0]*m for _ in range(n)]
        Max = 0
        
        
        for i in range(n):
            if matrix[i][0]=='1':
                dp[i][0] = 1  
                Max = max(dp[i][0],Max)
                
        for i in range(m):
            if matrix[0][i]=='1':
                dp[0][i] = 1 
                Max = max(dp[0][i],Max)
            
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]=='1':
                    dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    Max = max(Max,dp[i][j])
                    
        return Max**2