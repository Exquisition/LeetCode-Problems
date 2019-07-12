class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return None
        
        i = 0
        end = len(nums)
        
        while(i < end):

            if nums[i] == 0:
                
                # remove 0s from array and add to beginning
                popped = nums.pop(i)
                nums.insert(0,popped)

                
            elif nums[i] == 2:
                
                # remove 2s from array and add to end 
                popped = nums.pop(i)
                nums.append(popped)
                end -=1 
                i -=1 
            i+=1
        
        return nums
        