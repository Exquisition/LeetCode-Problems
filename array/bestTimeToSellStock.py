class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        """
        
        lowest = float('inf'); profit = 0
        
        for price in prices:
            profit = max(profit, price-lowest)
            lowest = min(price, lowest)
         
        return profit
        
        
        '''
        ### correct procedure but timed out
        
        n = len(prices)
        
        buy_ind = 0
        sell_ind = len(prices) - 1
        
        max_profit = 0
        
        min_arr = [float("+inf")]*n
        max_arr = [float("-inf")]*n
        
        
        for i, ele in enumerate(min_arr):
            min_arr[i] = min(prices[:i+1])
            max_arr[sell_ind] = max(prices[sell_ind:])
            
            sell_ind -= 1
            
        for j in range(n):
            max_profit = max(max_profit, max_arr[j] - min_arr[j])
            
        

        return max_profit
        
        
        '''
      
        
        
        