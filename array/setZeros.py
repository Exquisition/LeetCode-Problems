class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        
         [
          [0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]
         ]

        [(0,0), (0, 3)]
    
        set row 0 to all zeros, set column 0 and column 3 to all zeros 

        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        zeros_location = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros_location.append((i, j))
                    
        rows_to_set_to_zero = set([tup[0] for tup in zeros_location])
        columns_to_set_to_zero = set([tup[1] for tup in zeros_location])
        
        for row in rows_to_set_to_zero:
            for i in range(n):
                matrix[row][i] = 0
                
        for column in columns_to_set_to_zero:
            for i in range(m):
                matrix[i][column] = 0
                
                
        return matrix
                
                

                    
        