class Solution(object):
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        
        Adapted to find the sizes of the islands as well, and how many of each size
        
        """
        self.count = 0
        
        numIslands = 0
        
        
        def dfs(grid, i, j):
            # base case for recursion
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
                return
            # every time we sink in a one, add one to the island size
            grid[i][j] = '0'
            
            self.count += 1

            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

            return self.count
        
        # dictionary of island sizes, {size: occurences}
        sizes = {}
        
        if grid == []:
            return numIslands
        
        a = len(grid)
        b = len(grid[0])
       
        
        for i in range(a):
            for j in range(b):
                if grid[i][j] == '1':
                    numIslands += 1
                    sizeofIsland = dfs(grid, i, j)
                    
                    # done counting the size of this island, reset count
                    self.count = 0
                    if sizeofIsland not in sizes:
                        sizes[sizeofIsland] = 1
                    else:
                        sizes[sizeofIsland] += 1
        
        
        print(sizes)
                    
        return numIslands
                    
   