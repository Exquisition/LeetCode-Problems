class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        '''
        current_max[i] = max(nums[i], current_max[i-1] * nums[i], current_min[i-1] * nums[i])\
        
        current_min[i] = max(nums[i], current_max[i-1] * nums[i], current_min[i-1] * nums[i])
        
        '''
        n = len(nums) 
        current_min = [nums[0]] * (n+1)
        current_max = [nums[0]] * (n+1)
        
    
        for i in range(1, n):
            current_max[i] = max(nums[i], current_max[i-1] * nums[i], current_min[i-1] * nums[i])
            current_min[i] = min(nums[i], current_max[i-1] * nums[i], current_min[i-1] * nums[i])
            
        max_positive = max(current_max)
        max_negative = max(current_min)
        
        return max(max_positive, max_negative)
            
        