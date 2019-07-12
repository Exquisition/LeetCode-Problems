class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        
        index = self.binarySearch(nums, target)

        if index == -1:
            return [-1,-1]
        
		# see how long the contiguous sequence of the target is
        l = r = index
        while l >= 0 and nums[l] == target:
            l -= 1
        while r < len(nums) and nums[r] == target:
            r += 1
        
        return [l+1, r-1]

    def binarySearch(self, nums, target):
        l = 0
        r = len(nums)
        
        while l < r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid+1
        return -1
        
        
        
        
        