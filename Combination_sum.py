class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # candidates.sort()
        res = []
        for i, c in enumerate(candidates):
            if c < target:
                for sub in self.combinationSum(candidates[i:], target - c):
                    res.append([c] + sub)
            elif c == target:
                res.append([c])

        return res

