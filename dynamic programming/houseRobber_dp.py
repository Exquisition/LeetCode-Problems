class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        
        dp = [None] * (len(nums)+1)
        
        dp[0] = 1
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])
        
        
        for i in range(3, len(nums)+1):
            
            # either rob the current house plus the earnings from the previous houses without triggering alarm,
            # or don't rob current house and just keep earnings from previous house
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        
        return dp[len(nums)]
        