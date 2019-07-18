class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        """
        [10,9,2,5,3,7,101,18]
        
        [2,3,5,7,9,10,18,101]
        """
        
        if not nums:
            return 0
        
        n = len(nums)
        
        dp = [1]*n
        
        for j in range(1, n):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
            
        
        return max(dp)
                
            
        