class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        ex.
        input = [1,2,3,4]
        left product = [1,2,6,24]
        right product = [24,24,12,4]
        result = [24,12,8,6]
        
        result[i] = leftproduct[i-1] * rightproduct[i+1]   if 0 < i < len(nums) -1
        '''
        #build left product
        left_product = []
        value = 1
        for i in range(len(nums)):
            value *= nums[i]
            left_product.append(value)
            
            
        # build right product
        right_product = [None]*len(nums)
        value = 1
        for i in range(len(nums)-1, -1, -1):
            value *= nums[i]
            right_product[i] = value
       
        #obtain result
        result = [None]*len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                result[i] = right_product[i+1]
            elif i == len(nums) - 1:
                result[i] = left_product[len(nums)-2]
            else:
                result[i] = left_product[i-1] * right_product[i+1] 
                
        return result
                
        
        