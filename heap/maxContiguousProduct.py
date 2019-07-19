import heapq as hq

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        # find max 5 elements that have greatest absolute value
        
        if len(nums) < 3:
            return False
        
        h = []
        g = []
        
        for n in nums:
            hq.heappush(h, n)
            hq.heappush(g, n)
            
        smallest2 = []
        largest3 = []
        
        for i in range(len(nums)):
            if i < 2:
                smallest2.append(hq.heappop(h))
            else:
                break
                
        for j in range(len(nums)):
            if j < len(nums)-3:
                hq.heappop(g)
            else:
                largest3.append(hq.heappop(g))
            
                
        max1, max2, max3 = largest3[2], largest3[1], largest3[0]
        min1, min2 = smallest2[1], smallest2[0]
        max_product = max(max1*max2*max3, max1*min1*min2)
        
        return max_product
        
        