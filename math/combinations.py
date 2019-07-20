class Solution:
    def dfs(self, i, path):
            if len(path) == self.k:
                self.combis.append(path)
                return

            for num in range(i + 1, self.n + 1):
                self.dfs(num, path + [num])

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.k = k
        self.n = n     
        self.combis = []

        for i in range(1, n + 1):
            self.dfs(i, [i])

        return self.combis

        