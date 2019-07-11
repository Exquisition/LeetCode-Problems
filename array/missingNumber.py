class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        actual_sum = 0
        expected_sum = 0
        for i in range(len(nums)+1):
            expected_sum += i
        
        for num in nums:
            actual_sum += num
        
        return expected_sum - actual_sum
            
        