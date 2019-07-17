class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
      
        coins = sorted(coins)
        dp = [amount+1]*(amount+1)
        
        # dp[i] = least amount of coins to make up i cents
        
        dp[0] = 0
        
        for i in range(1, amount+1):
            for denom in coins:
                if denom <= amount:
                    # simulate taking the coin
                    dp[i] = min(dp[i], 1 + dp[i-denom])
                    
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]
        
        
        
        
        
        
        
        
        '''
        
        ### GREEDY APPROACH
        
        if amount == 0:
            return 0
        
        
        coins = sorted(coins)
        
        current_denomination_ptr = len(coins)-1
        numCoins = 0
        
        amount_left = amount
        while amount_left > 0:
            if coins[current_denomination_ptr] <= amount_left:
                amount_left -= coins[current_denomination_ptr]
                numCoins += 1
            else:
                if current_denomination_ptr > 0:
                    current_denomination_ptr -= 1
                else:
                    return -1
        
        if amount_left > 0:
            return -1
        
        return numCoins
            
        '''
                
            
            
        
        