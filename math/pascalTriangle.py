class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        
        for i in range(numRows):
            res.append(self.rowN(i+1))
            
        return res
        
        
    def rowN(self, n):
        if n == 1:
            return [1]
        elif n == 2:
            return [1,1]
        else:
            res = [1]
            last_row = self.rowN(n-1)
            for i in range(len(last_row) - 1):
                res.append(last_row[i] + last_row[i + 1])
                
            return res + [1]
        
        
        