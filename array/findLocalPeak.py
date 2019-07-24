class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        i = 0
        j = len(nums) - 1
        
        while i < j:
            mid = (i+j)//2
            if nums[mid] < nums[mid+1]:
                i = mid + 1
            else:
                j = mid
        
        return i
            
        
        