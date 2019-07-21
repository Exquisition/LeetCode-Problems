class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return None
        
        # [5,6,0,1,2,3,4]
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[left] > nums[right]:
                if nums[mid+1] > nums[mid] and nums[mid] > nums[left]:
                    left = mid + 1
                elif nums[mid+1] > nums[mid] and nums[mid] < nums[left]:
                    right = mid
            else:
                return nums[0]
                
            
                
       